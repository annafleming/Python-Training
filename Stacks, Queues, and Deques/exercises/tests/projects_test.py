import unittest
from ..array_deque import ArrayDeque


class ProjectsExercisesTestCase(unittest.TestCase):

    def test_should_init_qeque(self):
        deque = ArrayDeque()
        self.assertEqual(deque.__class__.__name__, 'ArrayDeque')

    def test_should_return_true_if_empty(self):
        deque = ArrayDeque()
        self.assertTrue(deque.is_empty())

    def test_should_return_len0_if_empty(self):
        deque = ArrayDeque()
        self.assertEqual(len(deque), 0)

    def test_should_add_element_to_the_back_of_deque(self):
        deque = ArrayDeque()
        deque.add_last(1)
        self.assertEqual(deque.first(), 1)

    def test_should_add_element_to_the_front_of_deque(self):
        deque = ArrayDeque()
        deque.add_last(1)
        deque.add_first(2)
        self.assertEqual(deque.first(), 2)

    def test_should_return_last_element_of_deque(self):
        deque = ArrayDeque()
        deque.add_last(1)
        deque.add_first(2)
        self.assertEqual(deque.last(), 1)

    def test_should_remove_first_element_from_deque(self):
        deque = ArrayDeque()
        deque.add_last(1)
        deque.add_first(2)
        self.assertEqual(deque.delete_first(), 2)
        self.assertEqual(deque.first(), 1)
        self.assertEqual(len(deque), 1)

    def test_should_remove_last_element_from_deque(self):
        deque = ArrayDeque()
        deque.add_last(1)
        deque.add_first(2)
        self.assertEqual(deque.delete_last(), 1)
        self.assertEqual(deque.first(), 2)
        self.assertEqual(len(deque), 1)

    def test_should_increase_capacity_on_demand(self):
        deque = ArrayDeque()
        deque.add_last(1)
        deque.add_last(2)
        deque.add_last(3)
        self.assertEqual(len(deque), 3)
        self.assertEqual(deque._data, [1, 2, 3, None])

if __name__ == '__main__':
    unittest.main()