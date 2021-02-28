class InsertionSort:

    def __init__(self, arr):
        self._arr = arr
        self._key = None

    def sort(self):
        for i in self._key_range():
            self._set_key(i)
            for j in self._before_key_range():
                if self._value_less_at_key(j):
                    self._swap_keys(j)
                    self._set_key(j)
        return self._arr

    def _swap_keys(self, j):
        tmp = self._arr[j]
        self._arr[j] = self._arr[self._key]
        self._arr[self._key] = tmp

    def _value_less_at_key(self, j):
        return self._arr[self._key] < self._arr[j]

    def _key_range(self):
        return range(1, len(self._arr))

    def _before_key_range(self):
        return range(self._key-1, -1, -1)

    def _set_key(self, k):
        self._key = k
