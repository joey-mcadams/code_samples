from unittest import TestCase
from kangaroo import kangaroo


class TestKangaroo(TestCase):
    def test_one(self):
        result = kangaroo(1, 1, 2, 2)
        self.assertEqual(result, "NO")
        pass
    def test_two(self):
        result = kangaroo(1, 2, 3, 1)
        self.assertEqual(result, "YES")

    def test_three(self):
        result = kangaroo(1, 6, 2, 2)
        self.assertEqual(result, "NO")

    def test_four(self):
        result = kangaroo(1, 10, 1000, 1)
        self.assertEqual(result, "YES")

