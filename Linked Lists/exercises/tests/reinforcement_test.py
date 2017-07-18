import unittest
from .. import reiforcement
from ..linked_queue import LinkedQueue


class ReinforcementExercisesTestCase(unittest.TestCase):

    def test_should_populate_linked_list(self):
        queue = reiforcement.populate_linked_list(LinkedQueue(), [1, 2, 3, 4, 5])
        self.assertEqual(queue.first(), 1)
        self.assertEqual(len(queue), 5)

    def test_should_return_second_to_last_element_in_singly_linked_list(self):
        queue = reiforcement.populate_linked_list(LinkedQueue(), [1, 2, 3, 4, 5])
        self.assertEqual(reiforcement.get_second_to_last(queue), 4)

    def test_should_concatenate_two_linked_lists(self):
        L = reiforcement.populate_linked_list(LinkedQueue(), [1, 2, 3])
        M = reiforcement.populate_linked_list(LinkedQueue(), [4, 5])
        C = reiforcement.concatenate_linked_lists(L, M)
        self.assertEqual(len(C), 5)
        self.assertEqual(C.first(), 1)
        self.assertEqual(reiforcement.get_second_to_last(C), 4)

    def test_should_recursively_count_nodes(self):
        L = reiforcement.populate_linked_list(LinkedQueue(), [1, 2, 3, 4, 5])
        self.assertEqual(reiforcement.recursively_count_nodes(L), 5)


        #R-7.4 





if __name__ == '__main__':
    unittest.main()