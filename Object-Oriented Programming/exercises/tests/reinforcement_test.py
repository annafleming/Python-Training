import unittest
from .. import reinforcement


class ReinforcementExercisesTestCase(unittest.TestCase):

    def test_should_return_true_if_is_multiple(self):
        self.assertTrue(reinforcement.is_multiple(4, 2))

    def test_should_return_false_if_is_not_multiple(self):
        self.assertFalse(reinforcement.is_multiple(4, 3))

    def test_should_return_true_if_is_even(self):
        self.assertTrue(reinforcement.is_even(4))

    def test_should_return_false_if_is_odd(self):
        self.assertFalse(reinforcement.is_even(5))

    def test_should_return_min_max_tuple(self):
        self.assertEqual(reinforcement.minmax([3, 4, 5, 6]), (3, 6))

    def test_should_return_sum_of_squares(self):
        self.assertEqual(reinforcement.get_sum_of_squares(4), 14)

    def test_should_return_sum_of_squares_of_odd_numbers(self):
        self.assertEqual(reinforcement.get_sum_of_squares_of_odd_numbers(5), 10)

    def test_should_produce_range(self):
        expected = [50, 60, 70, 80]
        self.assertEqual(list(range(50, 90, 10)), expected)
        expected = [8, 6, 4, 2, 0, -2, -4, -6, -8]
        self.assertEqual(list(range(8, -9, -2)), expected)

    def test_should_produce_list_using_list_comprehension(self):
        expected = [1, 2, 4, 8, 16, 32, 64, 128, 256]
        self.assertEqual([2**i for i in range(9)], expected)

    def test_should_return_random_element_from_sequence(self):
        seq = [1, 2, 4, 8, 16, 32, 64, 128, 256]
        rand_element = reinforcement.get_rand_element(seq)
        self.assertIn(rand_element, seq)

if __name__ == '__main__':
    unittest.main()