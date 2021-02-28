from pytest import raises

from data_structures.queue.queue import Queue


class TestQueue:
    def test_initialization(self):
        queue = Queue()
        assert isinstance(queue, Queue)

    def test_initialized_queue_is_empty(self):
        queue = Queue()
        assert queue.empty()

    def test_initialized_queue_has_size_0(self):
        queue = Queue()
        assert queue.size() == 0

    def test_len_retrieves_queue_size(self):
        queue = Queue()
        assert len(queue) == queue.size()

    def test_queue_is_not_empty_after_enqueue(self):
        queue = Queue()
        queue.enqueue(0)
        assert not queue.empty()

    def test_queue_size_matches_number_of_enqueues(self):
        queue = Queue()
        assert len(queue) == 0
        queue.enqueue(0)
        assert len(queue) == 1
        queue.enqueue(1)
        queue.enqueue(2)
        assert len(queue) == 3

    def test_queue_size_is_reduced_by_dequeue(self):
        queue = Queue()
        queue.enqueue(0)
        queue.enqueue(1)
        queue.enqueue(2)
        assert len(queue) == 3

        queue.dequeue()
        assert len(queue) == 2
        queue.dequeue()
        queue.dequeue()
        assert len(queue) == 0

    def test_dequeue_empty_queue_raises_empty_queue_exception(self):
        queue = Queue()
        with raises(Queue.EmptyQueueException):
            queue.dequeue()

        queue = Queue()
        queue.enqueue(0)
        queue.dequeue()
        with raises(Queue.EmptyQueueException):
            queue.dequeue()

    def test_get_front_of_empty_queue_raises_empty_queue_exception(self):
        queue = Queue()
        with raises(Queue.EmptyQueueException):
            queue.front()

    def test_front_of_non_empty_queue_returns_first_in_value(self):
        queue = Queue()
        queue.enqueue(0)
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.front() == 0
        queue.dequeue()
        assert queue.front() == 1

    def test_get_rear_of_empty_queue_raises_empty_queue_exception(self):
        queue = Queue()
        with raises(Queue.EmptyQueueException):
            queue.rear()

    def test_rear_of_non_empty_queue_returns_last_in_value(self):
        queue = Queue()
        queue.enqueue(0)
        assert queue.rear() == 0
        queue.enqueue(1)
        assert queue.rear() == 1
        queue.enqueue(2)
        assert queue.rear() == 2
