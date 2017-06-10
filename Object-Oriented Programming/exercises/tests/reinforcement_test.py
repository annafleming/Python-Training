import unittest
from ..reinforcement.flower import Flower
from ..reinforcement.credit_card import CreditCard
from ..reinforcement.vector import Vector

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

    def test_should_subtract_two_vectors(self):
        v = Vector(4)
        v[0] = 10
        u = Vector(4)
        u[0] = 3
        expected_v = Vector(4)
        expected_v[0] = 7
        self.assertEqual(v-u, expected_v)

    def test_should_negate_vector_coords(self):
        v = Vector(4)
        v[0] = 10
        expected_v = Vector(4)
        expected_v[0] = -10
        self.assertEqual(-v, expected_v)

    def test_should_multiply_vector_by_scalar(self):
        v = Vector(3)
        v[0] = 1
        v[1] = 2
        v[2] = 3
        expected_v = Vector(3)
        expected_v[0] = 3
        expected_v[1] = 6
        expected_v[2] = 9
        self.assertEqual(v * 3, expected_v)
        self.assertEqual(3 * v, expected_v)

    def test_should_multiply_two_vectors(self):
        v = Vector(3)
        v[0] = 1
        v[1] = 2
        v[2] = 3
        u = Vector(3)
        u[0] = 2
        u[1] = 2
        u[2] = 2
        expected_v = Vector(3)
        expected_v[0] = 2
        expected_v[1] = 4
        expected_v[2] = 6
        self.assertEqual(v * u, expected_v)
        self.assertEqual(u * v, expected_v)

    def test_should_instantiate_vector_when_given_sequence(self):
        u = Vector([1, 2, 3])
        v = Vector(3)
        v[0] = 1
        v[1] = 2
        v[2] = 3
        self.assertEqual(v, u)

if __name__ == '__main__':
    unittest.main()