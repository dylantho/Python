import unittest
from gui_assignment_orig import NumberGuesser


class MyTestCase(unittest.TestCase):
    # Test 1: Required parameters Status: Pass
    def setUp(self):
        self.numbguess = NumberGuesser([])

    def test_object_created_const(self):
        self.assertEqual(self.numbguess.guessed_list, [])

    def test_add_guess(self):
        self.numbguess.add_guess(5)
        self.numbguess.add_guess(8)
        self.assertEqual(self.numbguess.guessed_list, [5, 8])

    def tearDown(self):
        del self.numbguess


if __name__ == '__main__':
    unittest.main()
