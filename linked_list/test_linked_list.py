from unittest import TestCase
from linked_list import LinkedList


class TestLinkedList(TestCase):
    def test_basic_test(self):
        ll = LinkedList()
        ll.add_first("A")
        ll.add_last("B")
        ll.print()
        result = ll.return_as_list()
        self.assertEqual(result, ["A", "B"])

    def test_reverse_list(self):
        ll = LinkedList()
        ll.add_first("B")
        ll.add_first("A")
        ll.add_last("C")
        ll.reverse()
        ll.print()
        result = ll.return_as_list()
        self.assertEqual(result, ["C", "B", "A"])

    def test_sort_list(self):
        ll = LinkedList()
        ll.add_first("B")
        ll.add_first("C")
        ll.add_last("A")
        ll.sort_descending()
        ll.print()
        result = ll.return_as_list()
        self.assertEqual(result, ["A", "B", "C"])
