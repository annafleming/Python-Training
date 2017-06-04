import unittest
from .. import projects


class ProjectsExercisesTestCase(unittest.TestCase):

    def test_should_reverse_list(self):
        self.assertEqual(projects.make_change(35, 50), [10, 5])
        self.assertEqual(projects.make_change(1, 50), [20, 20, 5, 1, 1, 1, 1])

if __name__ == '__main__':
    unittest.main()