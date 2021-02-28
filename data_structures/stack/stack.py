class Stack:
    def __init__(self):
        self._list = []

    def __len__(self):
        return self.size()

    def empty(self):
        return not self._list

    def size(self):
        return len(self._list)

    def push(self, value):
        self._list.append(value)

    def top(self):
        if self._list:
            return self._list[-1]
        else:
            raise Stack.EmptyStackException

    def pop(self):
        v = self.top()
        del self._list[-1]
        return v

    class EmptyStackException(Exception):
        """Raised when accessing value from an empty stack."""
