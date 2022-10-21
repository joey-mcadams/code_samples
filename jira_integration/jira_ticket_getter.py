import requests
import os
import json
import logging
from requests.auth import HTTPBasicAuth
from elasticsearch import Elasticsearch
from time import sleep

logging.basicConfig(level = logging.INFO)


# TODO: Make JiraConnectionBaseClass
class JiraTicketGetter:
    def __init__(self):
        config_dict = self._read_config()

        self.basic_auth = HTTPBasicAuth(config_dict.get("user_id"), config_dict.get("api_key"))
        self.base_url = f"https://{config_dict.get('tenant')}.atlassian.net"
        self.project_key = config_dict.get('project_key')
        self.elastic_client = None
        self._connect_elastic()

        self.logger = logging.getLogger()

    def _connect_elastic(self):
        """
        Util function for testing. This will allow us to test the Elastic connection independently.

        :return: None
        """
        # TODO: This should be configurable, but assume a local host here.
        self.elastic_client = Elasticsearch("http://localhost:9200")
        return self.elastic_client.info()

    def _read_config(self):
        """
        Read the initial configuration.

        :return: Config dict
        """
        current_path = os.path.dirname(os.path.realpath(__file__))
        current_path += "/jira_cfg.json"
        with open(current_path) as f:
            content = f.read()
        return json.loads(content)

    def _test_connection(self) -> bool:
        """
        This function tests the integration to verify credentials are good.

        :return:True if connected, false if not
        """

        url = f"{self.base_url}/rest/api/2/serverInfo"
        result = requests.get(url, auth=self.basic_auth)

        # TODO: Catch this and do something reasonable with it.
        result.raise_for_status()
        return True

    def get_high_and_higher_tickets_beyond_last_ticket(self, project_name: str, last_ticket_id: int) -> list:
        """
        This will only return high or higher priority tickets greater than the last ID provided.

        :return: An object containing all tickets.
        """
        url = f"{self.base_url}/rest/api/2/search"

        # TODO: Externalize priorities
        params = {
            "jql": f"project = {project_name} AND id > {last_ticket_id} AND (priority = High OR priority = Highest) ORDER BY id ASC"
        }
        result = requests.get(url, auth=self.basic_auth, params=params)
        try:
            result.raise_for_status()
        except Exception as e:
            if "Issue does not exist or you do not have permission to see it." in result.text:
                pass  # We don't have any issues yet.
            else:
                raise e

        return result.json().get("issues", [])

    def get_most_recent_ticket(self, project_name: str) -> int:
        """
        This will return the ID of the most recent ticket in Jira

        :return: An object containing all tickets.
        """
        url = f"{self.base_url}/rest/api/2/search"
        params = {
            "jql": f"project = {project_name} ORDER BY id DESC"
        }
        result = requests.get(url, auth=self.basic_auth, params=params)
        result.raise_for_status()

        # Return the top ID or 0 if no issues are found.
        issues = result.json().get("issues")
        if len(issues) > 0:
            ticket_id = issues[0].get("id")
        else:
            ticket_id = 0

        return ticket_id

    def main(self, run_for_seconds: int) -> None:
        """
        Main Loop

        :param run_for_seconds: Number of seconds to run
        :return:
        """
        most_recent_id = self.get_most_recent_ticket(self.project_key)

        # I couldn't think of a good end condition. CTRL-C it is.
        time_counter = 0
        loop_time = 10
        while time_counter < run_for_seconds:
            self.logger.info("Getting new tickets.")
            new_tickets = self.get_high_and_higher_tickets_beyond_last_ticket(self.project_key, most_recent_id)
            for ticket in new_tickets:
                self.logger.info(f"New tickets found, pushing to ElasticSearch. Ticket ID: {ticket.get('id')}")
                self.elastic_client.index(index="jira_tickets", id=ticket.get("id"), document=ticket)
                most_recent_id = ticket.get('id')  # These should come back in ascending order, the last one will be the most recent ID.
            else:
                self.logger.info(f"No new tickets found. Last ID was: {most_recent_id}")
            sleep(loop_time)
            time_counter += loop_time


if __name__ == "__main__":
    run_for = 3600  # Number of seconds to run.
    jira_ticket_getter = JiraTicketGetter()
    jira_ticket_getter.main(run_for)


