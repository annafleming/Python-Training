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

    def test_should_produce_list_using_list_comprehension(self):
        expected = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
        self.assertEqual([i**2 - i for i in range(1, 11)], expected)

    def test_should_generate_alphabet(self):
        expected = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                    'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z']
        self.assertEqual([chr(i) for i in range(ord('a'), ord('z') + 1)], expected)

    def test_should_implement_random_shuffle(self):
        seq = [1, 2, 3, 4, 5]
        shuffled = creativity.shuffle(seq)
        self.assertNotEqual(shuffled, seq)

    def test_should_return_dot_product_of_two_arrays(self):
        seq1 = [1, 2, 3, 4, 5]
        seq2 = [2, 2, 2, 2, 2]
        expected = [2, 4, 6, 8, 10]
        self.assertEqual(creativity.get_dot_product(seq1, seq2), expected)

    def test_should_return_out_of_bounds_exception(self):
        self.assertEqual(creativity.insert_element_by_index([2, 3, 4], 5, 'Value'),
                         "Don’t try buffer overflow attacks in Python!")

    def test_should_count_vowels(self):
        self.assertEqual(creativity.count_vowels('alba'), 2)

    def test_should_remove_punctuation(self):
        self.assertEqual(creativity.remove_punctuation("Let's try, Mike."), "Lets try Mike")

if __name__ == '__main__':
    unittest.main()