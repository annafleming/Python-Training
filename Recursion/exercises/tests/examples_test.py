import unittest
from .. import examples


class RecursionExamplesTestCase(unittest.TestCase):

    def test_should_return_true_if_value_is_found(self):
        sequence = [1, 4, 6, 7, 8, 9, 10]
        self.assertTrue(examples.in_list(sequence, 9))
        sequence = [1, 4, 6, 7, 8, 9, 10, 11]
        self.assertTrue(examples.in_list(sequence, 11))
        sequence = [1, 4, 6, 7, 8, 9, 10, 11]
        self.assertTrue(examples.in_list(sequence, 1))

    def test_should_return_false_if_value_is_not_found(self):
        sequence = [1, 4, 6, 7, 8, 9, 10]
        self.assertFalse(examples.in_list(sequence, 5))

if __name__ == '__main__':
    unittest.main()