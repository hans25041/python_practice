class Queue:
    def __init__(self):
        self._list = []

    def __len__(self):
        return self.size()

    def empty(self):
        return len(self) == 0

    def size(self):
        return len(self._list)

    def enqueue(self, value):
        self._list.append(value)

    def dequeue(self):
        self._raise_exception_if_empty()
        del self._list[0]

    def front(self):
        self._raise_exception_if_empty()
        return self._list[0]

    def rear(self):
        self._raise_exception_if_empty()
        return self._list[-1]


    def _raise_exception_if_empty(self):
        if self.empty():
            raise Queue.EmptyQueueException

    class EmptyQueueException(Exception):
        """Raised when trying to access element of empty Queue."""
