from pytest import raises

from data_structures.heap.maxheap import MaxHeap


class TestHeap:
    def test_initialization(self):
        heap = MaxHeap()
        assert isinstance(heap, MaxHeap)

    def test_find_max_of_empty_heap_raises_exception(self):
        heap = MaxHeap()
        with raises(MaxHeap.EmptyHeapException):
            heap.find_max()

    def test_extract_max_of_empty_heap_raises_exception(self):
        heap = MaxHeap()
        with raises(MaxHeap.EmptyHeapException):
            heap.extract_max()

    def test_delete_max_of_empty_heap_raises_exception(self):
        heap = MaxHeap()
        with raises(MaxHeap.EmptyHeapException):
            heap.delete_max()

    def test_size_of_empty_heap_is_0(self):
        heap = MaxHeap()
        assert heap.size() == 0

    def test_empty_heap_is_empty(self):
        heap = MaxHeap()
        assert heap.is_empty()

    def test_heap_is_not_empty_after_insert(self):
        heap = MaxHeap()
        heap.insert(0)
        assert not heap.is_empty()

    def test_heap_size_is_1_after_single_push(self):
        heap = MaxHeap()
        heap.insert(0)
        assert heap.size() == 1

    def test_heap_size_is_3_after_three_pushes(self):
        heap = MaxHeap()
        heap.insert(0)
        heap.insert(1)
        heap.insert(2)
        assert heap.size() == 3

    def test_after_single_push_find_max_returns_value(self):
        heap = MaxHeap()
        heap.insert(0)
        assert heap.find_max() == 0

    def test_after_single_push_delete_max_removes_the_value(self):
        heap = MaxHeap()
        heap.insert(0)
        assert heap.size() == 1
        assert not heap.is_empty()
        heap.delete_max()
        assert heap.size() == 0
        assert heap.is_empty()

    def test_after_single_push_extract_max_removes_and_returns_value(self):
        heap = MaxHeap()
        heap.insert(0)
        assert heap.size() == 1
        assert not heap.is_empty()
        assert heap.extract_max() == 0
        assert heap.size() == 0
        assert heap.is_empty()

    def test_after_two_pushes_find_max_finds_larger_value(self):
        heap = MaxHeap()
        heap.insert(0)
        heap.insert(1)
        assert heap.find_max() == 1

    def test_two_pushes_and_two_extract_max_correct_values_empty_at_end(self):
        heap = MaxHeap()
        heap.insert(0)
        heap.insert(1)

        assert heap.size() == 2
        assert not heap.is_empty()
        assert heap.extract_max() == 1
        assert heap.size() == 1
        assert not heap.is_empty()
        assert heap.extract_max() == 0
        assert heap.size() == 0
        assert heap.is_empty()
