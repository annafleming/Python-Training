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

    def test_should_return_all_subsets_with_1_element(self):
        sequence = [1]
        self.assertEqual(creativity.get_subsets(sequence), [[1]])

    def test_should_return_all_subsets_with_2_elements(self):
        sequence = [1, 2]
        self.assertEqual(creativity.get_subsets(sequence), [[2], [1], [2, 1]])

    def test_should_return_all_subsets_with_3_elements(self):
        sequence = [1, 2, 3]
        self.assertEqual(creativity.get_subsets(sequence), [[3], [2], [3, 2], [1], [3, 1], [2, 1], [3, 2, 1]])


class TowersOfHanoiExercisesTestCase(unittest.TestCase):
    def test_should_work_with_n_1(self):
        source = [1]
        expected = list(source)
        target = []
        helper = []
        self.assertEqual(creativity.moveDiscs(len(source), source, target, helper), expected)

    def test_should_work_with_n_2(self):
        source = [2, 1]
        expected = list(source)
        target = []
        helper = []
        self.assertEqual(creativity.moveDiscs(len(source), source, target, helper), expected)

    def test_should_work_with_n_6(self):
        source = [6,5,4,3,2,1]
        expected = list(source)
        target = []
        helper = []
        self.assertEqual(creativity.moveDiscs(len(source), source, target, helper), expected)

    def test_should_reverse_a_string(self):
        self.assertEqual(creativity.reverse_string('pots&pans'), 'snap&stop')

    def test_is_palindrome(self):
        self.assertTrue(creativity.is_palindrome('racecar'))
        self.assertFalse(creativity.is_palindrome('raceca'))
        self.assertTrue(creativity.is_palindrome('raceecar'))

    def test_should_define_more_vowels(self):
        self.assertEqual(creativity.has_more_vowels('acaca'), 1)
        self.assertEqual(creativity.has_more_vowels('acac'), 0)
        self.assertEqual(creativity.has_more_vowels('acacc'), -1)

    def test_should_sort_sequence_so_even_go_first(self):
        self.assertEqual(creativity.sort_even_first([1]), [1])
        self.assertEqual(creativity.sort_even_first([1, 2]), [2, 1])
        self.assertEqual(creativity.sort_even_first([1, 2, 3, 4]), [2, 4, 3, 1])


if __name__ == '__main__':
    unittest.main()