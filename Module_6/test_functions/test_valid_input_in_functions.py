import unittest
from validate_input_in_functions import score_input

class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(score_input("Exam 1"), "Exam 1: 0")


    def test_score_input_test_score_valid(self):
        self.assertEqual(score_input("Exam 2", 75), "Exam 2: 75")
    def test_score_input_test_score_below_range(self):
        self.assertEqual(score_input("Exam 3", -25), "Invalid test score, try again!")
    def test_score_input_test_score_above_range(self):
        self.assertEqual(score_input("Exam 4", 215), "Invalid test score, try again!")
    def test_score_input_test_score_non_numeric(self):
        self.assertEqual(score_input("Exam 5", "hello"), "Invalid test score, try again!")

    def test_score_input_invalid_message(self):
        self.assertEqual(score_input("Exam 5", -50, "That is not a valid input, try again!"), "That is not a valid input, try again!")



if __name__ == '__main__':
    unittest.main()
