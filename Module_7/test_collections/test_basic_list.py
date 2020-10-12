import unittest
from unittest.mock import patch
from basic_list import make_list


class TestList(unittest.TestCase):
    @patch('basic_list.get_input', return_value='3')
    def test_make_list(self, input):
        self.assertEqual(make_list(), [3, 3, 3])


if __name__ == '__main__':
    unittest.main()
