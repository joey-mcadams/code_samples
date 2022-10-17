from unittest import TestCase
from .jira_ticket_maker import JiraTicketMaker


class TestJiraTicketMaker(TestCase):
    def setUp(self) -> None:
        self.test_object = JiraTicketMaker()

    def test_read_config(self):
        result = self.test_object._read_config()
        self.assertIn("user_id", result.keys())

    def test_test_connection(self):
        self.test_object._test_connection()
        # Pass, fail on exception

    def test_get_priorities(self):
        result = self.test_object.get_all_priorities()
        self.assertIsNotNone(result)

    def test_create_ticket(self):
        for i in range(0,10):
            result = self.test_object.create_random_ticket("FAKEKEY")
            self.assertTrue(result.get('priority') in self.test_object.priorities)

    def test_post_ticket_to_jira(self):
        ticket = self.test_object.create_random_ticket("JOEYT")
        self.test_object.post_ticket_to_jira(ticket)