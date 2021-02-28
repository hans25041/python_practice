class Node:
    def __init__(self, data=None, _next=None):
        self.data = data
        self.next = _next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def __getitem__(self, key):
        def get_nth_node(node, i):
            if not node:
                raise IndexError
            if i == 0:
                return node
            return get_nth_node(node.next, i - 1)

        return get_nth_node(self.head, key)

    def __contains__(self, data):
        node = self.head
        while node:
            if node.key == data:
                return True
            node = node.next
        return False

    @classmethod
    def from_list(cls, starting_list):
        linked_list = cls()
        last_node = None
        for el in starting_list:
            node = Node(el)
            if not linked_list.head:
                linked_list.head = node
            else:
                last_node.next = node
            last_node = node
        return linked_list

    def to_list(self):
        result = []
        node = self.head
        while node:
            result.append(node.key)
            node = node.next
        return result

    def push(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_after_index(self, index, data):
        self.insert_after(self[index], data)

    @staticmethod
    def insert_after(node, data):
        node.next = Node(data, node.next)

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            self[index-1].next = self[index].next
