from unittest import TestCase
from .interpretor import *


class TestInterpretor(TestCase):

    def test_run_program(self):
        test_bytes = [1, 1, 3, 1, 5, 1, 1, 100, 86, 0, 1, 100]
        initial_value = 0
        result = run_program(initial_value, test_bytes)
        self.assertEqual(result, 0)

