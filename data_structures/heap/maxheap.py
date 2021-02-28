class MaxHeap:

    def __init__(self):
        self._arr = []

    def insert(self, value):
        self._arr.append(value)
        self._heapify()

    def find_max(self):
        self._raise_empty_heap_exception_if_empty()
        return self._arr[0]

    def extract_max(self):
        self._raise_empty_heap_exception_if_empty()
        value = self.find_max()
        self.delete_max()
        return value

    def delete_max(self):
        self._raise_empty_heap_exception_if_empty()
        self._arr.pop(0)

    def size(self):
        return len(self._arr)

    def is_empty(self):
        return self.size() == 0

    def _raise_empty_heap_exception_if_empty(self):
        if self.is_empty():
            raise MaxHeap.EmptyHeapException

    def _heapify(self):
        for i in range(self.size()):
            if self._left(i) and self._left(i) > self._at(i):
                self._swap_left(i)
            if self._right(i) and self._right(i) > self._at(i):
                self._swap_right(i)

    def _swap_left(self, i):
        key = self._left_key(i)
        self._swap(i, key)

    def _swap_right(self, i):
        key = self._right_key(i)
        self._swap(i, key)

    def _swap(self, i, key):
        tmp = self._at(key)
        self._arr[key] = self._at(i)
        self._arr[i] = tmp

    def _at(self, i):
        if i < self.size():
            return self._arr[i]
        else:
            return None

    def _left(self, i):
        key = self._left_key(i)
        return self._at(key)

    @staticmethod
    def _left_key(i):
        return 2*i + 1

    def _right(self, i):
        key = self._right_key(i)
        return self._at(key)

    @staticmethod
    def _right_key(i):
        return 2*i + 2

    class EmptyHeapException(Exception):
        """Raised when accessing elements in an empty Heap."""
