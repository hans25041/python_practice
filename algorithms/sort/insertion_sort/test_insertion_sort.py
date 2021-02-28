from algorithms.sort.insertion_sort.insertion_sort import InsertionSort


class TestInsertionSort:
    def test_initialization(self):
        sorter = InsertionSort([])
        assert isinstance(sorter, InsertionSort)

    def test_sorted_list_returns_unchanged(self):
        sorted_list = [1, 2, 3, 4, 5]
        sorter = InsertionSort(sorted_list)
        assert sorter.sort() == sorted_list

    def test_reverse_sorted_list_returns_in_correct_order(self):
        reversed_list = [5, 4, 3, 2, 1]
        sorter = InsertionSort(reversed_list)
        assert sorter.sort() == [1, 2, 3, 4, 5]

    def test_unsorted_list_is_sorted_correctly(self):
        unsorted_list = [4, 2, 3, 5, 1]
        sorter = InsertionSort(unsorted_list)
        assert sorter.sort() == [1, 2, 3, 4, 5]
