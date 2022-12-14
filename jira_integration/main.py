#
import threading
import os
import time
import logging
from jira_ticket_getter import JiraTicketGetter
from jira_ticket_maker import JiraTicketMaker
from flask_app import app


class Main:
    def run_application(self):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger()

        full_command = "docker run -d -p 5601:5601 -p 9200:9200 -p 5044:5044 sebp/elk"
        logger.info(f"{full_command}")
        os.system(full_command)
        logger.info("Started Docker, sleeping for 60 seconds.")
        time.sleep(60)  # TODO: there's got to be a better way to do this.
        logger.info("Done sleeping, starting Jira integrations.")

        getter = JiraTicketGetter()
        maker = JiraTicketMaker()

        getter_thread = threading.Thread(target=getter.main, args=(3600,))
        maker_thread = threading.Thread(target=maker.main, args=(100,))

        # flask_thread = threading.Thread(target=app.run)

        logger.info("Starting threads.")
        getter_thread.start()
        maker_thread.start()
        # flask_thread.start()  # matlabplot bombs if it's not in the main thead.
        logger.info("Everything running.")

        app.run()  # This makes an infinite block

        getter_thread.join()
        maker_thread.join()

        full_command = "docker stop sebp/elk"
        os.system(full_command)


if __name__ == "__main__":
    Main().run_application()

