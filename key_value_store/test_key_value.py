from unittest import TestCase
from key_value import KeyValue


class TestKeyValue(TestCase):
    def setUp(self):
        self.kv_test = KeyValue()

    def test_add(self):
        self.kv_test.set_value("a", 10)
        result = self.kv_test.get_value("a")
        self.assertEqual(result, 10)

    def test_add(self):
        self.kv_test.set_value("a", 10)
        self.kv_test.delete_key("a")
        result = self.kv_test.get_value("a")
        self.assertIsNone(result)

    def test_count(self):
        self.kv_test.set_value("a", 10)
        self.kv_test.set_value("b", 10)
        result = self.kv_test.count(10)
        self.assertEqual(result, 2)

        self.kv_test.set_value("a", 20)
        result = self.kv_test.count(10)
        self.assertEqual(result, 1)

