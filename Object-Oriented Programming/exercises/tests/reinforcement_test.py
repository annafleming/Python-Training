import unittest
from ..reinforcement.flower import Flower
from ..reinforcement.credit_card import CreditCard

class ReinforcementExercisesTestCase(unittest.TestCase):

    def test_should_instantiate_class_flower_with_params(self):
        flower = Flower('rose', 4, 35.3)
        self.assertIsInstance(flower, Flower)

    def test_should_set_and_get_price_for_flower(self):
        flower = Flower('rose', 4, 35.3)
        flower.set_price(50)
        self.assertEqual(flower.get_price(), 50)

    def test_should_throw_error_if_not_number_charged(self):
        cc = CreditCard('JohnDoe', '1st Bank', 5391037593875309, 1000)
        with self.assertRaises(Exception) as error:
            cc.charge('dddd')
        self.assertEqual(str(error.exception), 'Charged amount should be a number')

    def test_should_raise_error_if_negative_payment_sent(self):
        cc = CreditCard('JohnDoe', '1st Bank', 5391037593875309, 1000)
        with self.assertRaises(ValueError) as error:
            cc.make_payment(-49)
        self.assertEqual(str(error.exception), 'Payment amount cannot be negative')

    def test_should_set_balace_to_zero_if_not_passed(self):
        cc = CreditCard('JohnDoe', '1st Bank', 5391037593875309, 1000)
        self.assertEqual(cc.get_balance(), 0)

    def test_should_set_balace_value_if_passes(self):
        cc = CreditCard('JohnDoe', '1st Bank', 5391037593875309, 1000, 50)
        self.assertEqual(cc.get_balance(), 50)
        
if __name__ == '__main__':
    unittest.main()