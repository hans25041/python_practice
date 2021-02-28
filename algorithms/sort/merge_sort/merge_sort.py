from math import floor


class MergeSort:
    def __init__(self, arr):
        self._arr = arr

    def sort(self):
        if len(self._arr) == 1:
            return self._arr
        pivot = floor(len(self._arr)/2)
        left = MergeSort(self._arr[0:pivot]).sort()
        right = MergeSort(self._arr[pivot:]).sort()
        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        left_finger = self._draw(left)
        right_finger = self._draw(right)
        while True:
            if right_finger is None and left_finger is None:
                break
            elif left_finger is None:
                res.append(right_finger)
                right_finger = self._draw(right)
            elif right_finger is None:
                res.append(left_finger)
                left_finger = self._draw(left)
            elif left_finger < right_finger:
                res.append(left_finger)
                left_finger = self._draw(left)
            else:
                res.append(right_finger)
                right_finger = self._draw(right)
        return res

    @staticmethod
    def _draw(arr):
        try:
            return arr.pop(0)
        except IndexError:
            return None

