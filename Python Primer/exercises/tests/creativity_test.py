import unittest
from .. import creativity


class CreativityExercisesTestCase(unittest.TestCase):

    def test_should_reverse_list(self):
        list_of_int = [1, 2, 3, 4, 5]
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(creativity.reverse_list(list_of_int), expected)

if __name__ == '__main__':
    unittest.main()