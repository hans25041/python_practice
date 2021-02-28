from pytest import raises

from data_structures.stack.stack import Stack


class TestStack:
    def test_initialization(self):
        stack = Stack()
        assert isinstance(stack, Stack)

    def test_initialized_stack_is_empty(self):
        stack = Stack()
        assert stack.empty()

    def test_initialized_stack_has_size_0(self):
        stack = Stack()
        assert stack.size() == 0

    def test_size_retrieved_using_len(self):
        stack = Stack()
        assert len(stack) == stack.size()

    def test_top_of_empty_stack_is_empty_stack_exception(self):
        stack = Stack()
        with raises(Stack.EmptyStackException):
            stack.top()

    def test_stack_not_empty_after_push(self):
        stack = Stack()
        stack.push(0)
        assert not stack.empty()

    def test_stack_length_matches_number_of_pushes(self):
        stack = Stack()
        assert len(stack) == 0
        stack.push(0)
        assert len(stack) == 1
        stack.push(1)
        stack.push(2)
        assert len(stack) == 3

    def test_top_gets_last_pushed_value(self):
        stack = Stack()
        stack.push(0)
        assert stack.top() == 0
        stack.push(1)
        assert stack.top() == 1
        stack.push(2)
        assert stack.top() == 2

    def test_pop_returns_and_removes_last_pushed_value(self):
        stack = Stack()
        stack.push(0)
        stack.push(1)
        stack.push(2)

        assert len(stack) == 3
        assert stack.pop() == 2
        assert len(stack) == 2
        assert stack.pop() == 1
        assert len(stack) == 1
        assert stack.pop() == 0
        assert len(stack) == 0
        with raises(Stack.EmptyStackException):
            stack.pop()
