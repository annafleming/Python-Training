import unittest
from ..reinforcement.flower import Flower


class ReinforcementExercisesTestCase(unittest.TestCase):

    def test_should_instantiate_class_flower_with_params(self):
        flower = Flower('rose', 4, 35.3)
        self.assertIsInstance(flower, Flower)

    def test_should_set_and_get_price_for_flower(self):
        flower = Flower('rose', 4, 35.3)
        flower.set_price(50)
        self.assertEqual(flower.get_price(), 50)

if __name__ == '__main__':
    unittest.main()