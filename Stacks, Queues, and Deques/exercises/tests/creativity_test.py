import unittest
from ..array_stack import ArrayStack
from ..array_queue import ArrayQueue
from .. import creativity
from ..custom_exceptions import Empty,Full


class CreativityExercisesTestCase(unittest.TestCase):

    def test_should_throw_exception_if_stack_len_exceeded(self):
        stack = ArrayStack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        with self.assertRaises(Full) as error:
            stack.push(4)
        self.assertEqual(str(error.exception), 'Stack capacity is exceeded')

    def test_should_match_html_without_attributes(self):
        html = '<body><center><h1> The Little Boat </h1></center><p> The storm tossed the little boat like a cheap sneaker in an</p><ol><li> Will the salesman die? </li><li> What color is the boat? </li><li> And what about Naomi? </li></ol></body>'
        self.assertTrue(creativity.is_matched_html(html))

    def test_should_match_html_with_attributes(self):
        html = '<body><center><h1 attribute1="value1" attribute2="value2"> The Little Boat </h1></center></body>'
        self.assertTrue(creativity.is_matched_html(html))

    def test_should_throw_exception_if_queue_capacity_exceeded(self):
        queue = ArrayQueue(3)
        queue.enququeue(1)
        queue.enququeue(2)
        queue.enququeue(3)
        with self.assertRaises(Full) as error:
            queue.enququeue(4)
        self.assertEqual(str(error.exception), 'Queue capacity is exceeded')

    def test_should_rotate_elemnt_in_queue(self):
        queue = ArrayQueue()
        queue.enququeue(1)
        queue.enququeue(2)
        queue.enququeue(3)
        queue.rotate()
        self.assertEqual(queue.first(), 2)

if __name__ == '__main__':
    unittest.main()