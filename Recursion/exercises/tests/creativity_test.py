import unittest
from .. import creativity


class CreativityExercisesTestCase(unittest.TestCase):

    def test_should_return_min_max_value_in_sequence(self):
        sequence = [2, 1, 5, 4, 3]
        self.assertEqual(creativity.get_min_max(sequence), (1, 5))

        sequence = [1]
        self.assertEqual(creativity.get_min_max(sequence), (1, 1))

        sequence = [5, 5, 5, 6]
        self.assertEqual(creativity.get_min_max(sequence), (5, 6))

if __name__ == '__main__':
    unittest.main()