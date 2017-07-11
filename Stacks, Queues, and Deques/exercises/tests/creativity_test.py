import unittest
from ..array_stack import ArrayStack, Full

class CrativityExercisesTestCase(unittest.TestCase):

    def test_should_throw_exception_if_stack_len_exceeded(self):
        stack = ArrayStack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        with self.assertRaises(Full) as error:
            stack.push(4)
        self.assertEqual(str(error.exception), 'Stack capacity is exceeded')

if __name__ == '__main__':
    unittest.main()