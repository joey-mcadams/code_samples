from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def empty_list(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        node_itr = self.head
        while node_itr.next is not None:
            node_itr = node_itr.next

        node_itr.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        self.head = prev

    def sort_descending(self):
        node_itr = self.head
        swapped = False

        while node_itr is not None and node_itr.next is not None:
            if node_itr.data > node_itr.next.data:
                temp = node_itr.next.data
                node_itr.next.data = node_itr.data
                node_itr.data = temp
                swapped = True
            node_itr = node_itr.next

        if swapped:
            self.sort_descending()

    def print(self):
        node_itr = self.head
        while node_itr is not None:
            print(node_itr.data)
            node_itr = node_itr.next

    def return_as_list(self):
        ret_list = []
        node_itr = self.head
        while node_itr is not None:
            ret_list.append(node_itr.data)
            node_itr = node_itr.next

        return ret_list


