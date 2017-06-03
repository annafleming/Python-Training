import unittest
from .. import creativity


class CreativityExercisesTestCase(unittest.TestCase):

    def test_should_reverse_list(self):
        list_of_int = [1, 2, 3, 4, 5]
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(creativity.reverse_list(list_of_int), expected)

    def test_has_product_odd_in_sequence(self):
        list_of_int = [1, 2, 3, 4, 5]
        self.assertTrue(creativity.has_product_odd([1, 2, 3, 4, 5]))
        self.assertFalse(creativity.has_product_odd([2, 4, 4, 6]))

    def test_has_product_odd_in_sequence_from_two_distinct_numbers(self):
        self.assertFalse(creativity.has_product_odd([3, 3, 2]))

    def test_should_determines_if_numbers_in_sequence_are_unique(self):
        self.assertTrue(creativity.are_numbers_unique([1, 2, 3, 4, 5]))
        self.assertFalse(creativity.are_numbers_unique([1, 2, 2, 4, 5]))


if __name__ == '__main__':
    unittest.main()