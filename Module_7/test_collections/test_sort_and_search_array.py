import unittest
import array
from sort_and_search_array import search_array
from sort_and_search_array import sort_array

class MyTestCase(unittest.TestCase):
    def test_search_array_item_found(self):
        self.assertEqual(search_array(array.array('i', [1, 2, 3, 4]), 4), 3)

    def test_search_array_item_not_found(self):
        self.assertEqual(search_array(array.array('i', [1, 2, 3, 4]), 46), -1)

    def test_search_array_sorted(self):
        self.assertEqual(sort_array([35, 75, -43, -65]), [-65, -43, 35, 75])


if __name__ == '__main__':
    unittest.main()
