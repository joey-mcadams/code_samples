import time
import requests
import os
import json
import sys
from random import randrange
from requests.auth import HTTPBasicAuth


class JiraTicketMaker():
    def __init__(self):
        config_dict = self._read_config()

        self.basic_auth = HTTPBasicAuth(config_dict.get("user_id"), config_dict.get("api_key"))
        self.base_url = f"https://{config_dict.get('tenant')}.atlassian.net"
        self.project_key = config_dict.get('project_key')
        self.priorities = ["Highest", "High", "Medium", "Low", "Lowest"]

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

    def get_all_priorities(self) -> list:
        """
        This will return a list of all priorities.

        :return: A list of priorities
        """
        url = f"{self.base_url}/rest/api/2/priority"
        result = requests.get(url, auth=self.basic_auth)
        result.raise_for_status()
        result.raise_for_status()
        return result.json()

    def create_random_ticket(self, project_key: str) -> dict:
        """
        Create a ticket given the project key.

        return: Random Ticket
        """
        epoch = int(time.time())

        priority = self.priorities[randrange(0, len(self.priorities))]
        ticket = {"fields":
            {
                'project': {
                    'key': project_key
                },
                'summary': f'Unit Test Ticket - {epoch}',
                'description': 'Unit test description - {epoch}',
                'issuetype': {
                    'name': 'Bug'
                },
                'priority': {
                    'name': priority
                }
            }
        }

        return ticket

    def post_ticket_to_jira(self, ticket: dict) -> None:
        """
        Post a ticket to Jira

        :param ticket: A ticket object
        :return: None
        """
        url = f"{self.base_url}/rest/api/2/issue"
        result = requests.post(url, json=ticket, auth=self.basic_auth)
        result.raise_for_status()

    def main(self, number_of_tickets: int):
        """
        This will raondomly create 1-2 tickets a second of random
        priorities and send them to jira.

        :return: None
        """
        total_tickets = 0
        while total_tickets < number_of_tickets:
            print(f"Sending ticket {total_tickets}")
            new_ticket = self.create_random_ticket(self.project_key)
            print(f"Ticket priority is: {new_ticket.get('fields').get('priority').get('name')}")
            self.post_ticket_to_jira(new_ticket)
            total_tickets += 1
            print(f"Ticket {total_tickets} sent!")
            delay = randrange(20, 40)
            print(f"Delay is: {delay}")
            time.sleep(delay)


if __name__ == "__main__":
    number_of_tickets = 100
    try:
        number_of_tickets = sys.argv[1]
    except IndexError:
        print("Setting default number of tickets to 100.")

    if not isinstance(number_of_tickets, int):
        print("Invalid argument. Please enter the number of tickets needed.")
        print("Example: jira_ticket_maker.py 100")
        exit(1)

    jira_ticket_thingy = JiraTicketMaker()
    jira_ticket_thingy.main(number_of_tickets)
