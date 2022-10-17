from unittest import TestCase
from .jira_ticket_getter import JiraTicketGetter


class TestJiraTicketMaker(TestCase):
    def setUp(self) -> None:
        self.test_object = JiraTicketGetter()

    def test_read_config(self):
        result = self.test_object._read_config()
        self.assertIn("user_id", result.keys())

    def test_test_connection(self):
        self.test_object._test_connection()

    def test_get_high_and_higher_tickets_beyond_last_ticket(self):
        result = self.test_object.get_high_and_higher_tickets_beyond_last_ticket("JoeyTestProject", 10042)
        self.assertIsInstance(result, list)
        self.assertTrue(result)  # len > 0

    def test_connect_elastic(self):
        result = self.test_object._connect_elastic()
        self.assertIsNotNone(result)

    def test_get_most_recent_ticket(self):
        result = self.test_object.get_most_recent_ticket(project_name="JoeyTestProject")
        self.assertIsInstance(result, int)

    def test_main(self):
        self.test_object.main(60)
        # Pass on no exceptions
