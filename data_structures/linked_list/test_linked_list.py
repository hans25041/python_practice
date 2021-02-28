from pytest import raises

from data_structures.linked_list.linked_list import Node, LinkedList


class TestNode:
    def test_initialization(self):
        node = Node()
        assert isinstance(node, Node)

    def test_node_has_value(self):
        node = Node("foo")
        assert node.data == "foo"

    def test_node_connects_to_other_nodes(self):
        bar_node = Node("bar")
        foo_node = Node("foo", _next=bar_node)
        assert foo_node.next == bar_node
        assert not bar_node.next


class TestLinkedList:
    def test_initialization(self):
        linked_list = LinkedList()
        assert isinstance(linked_list, LinkedList)

    def test_linked_list_with_head(self):
        node = Node("foo")
        linked_list = LinkedList(head=node)
        assert linked_list.head == node

    def test_create_linked_list_with_three_nodes(self):
        linked_list = LinkedList()

        linked_list.head = Node(1)
        second = Node(2)
        third = Node(3)

        assert linked_list.head.data == 1
        assert not linked_list.head.next
        assert not second.next
        assert not third.next

        linked_list.head.next = second
        second.next = third

        assert linked_list.head.next.data == 2
        assert linked_list.head.next.next.key == 3
        assert not linked_list.head.next.next.next

    def test_cast_linked_list_to_list(self):
        linked_list = LinkedList()
        third = Node(3)
        second = Node(2, third)
        first = Node(1, second)
        linked_list.head = first

        assert linked_list.to_list() == [1, 2, 3]

    def test_linked_list_from_list(self):
        starting_list = [1, 2, 3]
        linked_list = LinkedList.from_list(starting_list)
        assert linked_list.to_list() == starting_list
        assert linked_list.head.key == 1
        assert linked_list.head.next.key == 2
        assert linked_list.head.next.next.key == 3
        assert not linked_list.head.next.next.next

    def test_get_nodes_by_index(self):
        linked_list = LinkedList.from_list([1, 2, 3])
        assert linked_list[0] == linked_list.head
        assert linked_list[1] == linked_list.head.next
        assert linked_list[2] == linked_list.head.next.next
        with raises(IndexError):
            _ = linked_list[3]

    def test_push_a_node_to_the_start_of_a_linked_list(self):
        linked_list = LinkedList.from_list([1, 2, 3])
        linked_list.push(0)
        assert linked_list.to_list() == [0, 1, 2, 3]

    def test_push_to_an_empty_linked_list(self):
        linked_list = LinkedList()
        linked_list.push(0)
        assert linked_list.head.key == 0

    def test_insert_a_node_after_specified_node_in_a_linked_list(self):
        linked_list = LinkedList.from_list([1, 2, 4])
        linked_list.insert_after(linked_list[1], 3)
        assert linked_list.to_list() == [1, 2, 3, 4]

    def test_insert_a_node_after_last_node_in_a_linked_list(self):
        linked_list = LinkedList.from_list([1, 2, 3])
        linked_list.insert_after(linked_list[2], 4)
        assert linked_list.to_list() == [1, 2, 3, 4]

    def test_insert_a_node_after_an_index(self):
        linked_list = LinkedList.from_list([1, 2, 4])
        linked_list.insert_after_index(1, 3)
        assert linked_list.to_list() == [1, 2, 3, 4]

    def test_insert_a_node_after_the_final_index(self):
        linked_list = LinkedList.from_list([1, 2, 3])
        linked_list.insert_after_index(2, 4)
        assert linked_list.to_list() == [1, 2, 3, 4]

    def test_insert_a_node_after_an_invalid_index(self):
        linked_list = LinkedList.from_list([1, 2, 3])
        with raises(IndexError):
            linked_list.insert_after_index(10, 4)

    def test_append_a_node_to_a_linked_list(self):
        linked_list = LinkedList.from_list([1, 2, 3])
        linked_list.append(4)
        assert linked_list.to_list() == [1, 2, 3, 4]

    def test_append_to_an_empty_linked_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        assert linked_list.head.key == 1

    def test_delete_node_at_index(self):
        linked_list = LinkedList.from_list([1, 2, 3])
        linked_list.delete(1)
        assert linked_list.to_list() == [1, 3]

    def test_delete_node_at_head(self):
        linked_list = LinkedList.from_list([1, 2, 3])
        linked_list.delete(0)
        assert linked_list.to_list() == [2, 3]

    def test_delete_the_last_node(self):
        linked_list = LinkedList.from_list([1, 2, 3])
        linked_list.delete(2)
        assert linked_list.to_list() == [1, 2]

    def test_length_of_empty_linked_list_is_0(self):
        assert len(LinkedList()) == 0

    def test_length_of_non_empty_linked_list_is_number_of_nodes(self):
        linked_list = LinkedList.from_list([1, 2, 3, 4])
        assert len(linked_list) == 4

    def test_check_if_element_is_in_linked_list(self):
        linked_list = LinkedList.from_list([1, 2, 3])
        assert 1 in linked_list
        assert 2 in linked_list
        assert 3 in linked_list
        assert 4 not in linked_list
        assert 0 not in linked_list
