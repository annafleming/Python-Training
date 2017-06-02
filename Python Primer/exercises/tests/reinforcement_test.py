import unittest
from ..reinforcement import returns_false


class ReinforcementExercisesTestCase(unittest.TestCase):

    def test_primer(self):
        self.assertFalse(returns_false())

if __name__ == '__main__':
    unittest.main()