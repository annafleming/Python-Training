import unittest
from .. import reinforcement


class ReinforcementExercisesTestCase(unittest.TestCase):
    def test_should_transfer_stack(self):
        S = [1, 2, 3, 4]
        T = reinforcement.transfer(S)
        self.assertEqual(T, [4, 3, 2, 1])

    def test_should_clear_stack(self):
        result = reinforcement.clear_stack([1, 2, 3, 4])
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()