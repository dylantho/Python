import unittest
from unittest.mock import patch
from basic_list_exception import make_list


class TestList(unittest.TestCase):
    @patch('basic_list_exception.get_input', return_value='3')
    def test_make_list(self, input):
        self.assertEqual(make_list(), [3, 3, 3])


    @patch('basic_list_exception.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            make_list()

    @patch('basic_list_exception.get_input', return_value='-23')
    def test_make_list_below_range(self, input):
        with self.assertRaises(ValueError):
            make_list()

    @patch('basic_list_exception.get_input', return_value='82')
    def test_make_list_above_range(self, input):
        with self.assertRaises(ValueError):
            make_list()


if __name__ == '__main__':
    unittest.main()
