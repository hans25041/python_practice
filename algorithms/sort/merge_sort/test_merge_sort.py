from algorithms.sort.merge_sort.merge_sort import MergeSort


class TestMergeSort:
    def test_initialization(self):
        sorter = MergeSort([])
        assert isinstance(sorter, MergeSort)

    def test_sorted_list_returns_unchanged(self):
        sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]
        sorter = MergeSort(sorted_list)
        assert sorter.sort() == self._expected()

    def test_reverse_sorted_list_returns_in_correct_order(self):
        reversed_list = [8, 7, 6, 5, 4, 3, 2, 1]
        sorter = MergeSort(reversed_list)
        assert sorter.sort() == self._expected()

    def test_unsorted_list_is_sorted_correctly(self):
        unsorted_list = [6, 4, 2, 7, 3, 5, 1, 8]
        sorter = MergeSort(unsorted_list)
        assert sorter.sort() == self._expected()

    def _expected(self):
        return [1, 2, 3, 4, 5, 6, 7, 8]
