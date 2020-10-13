import unittest
from sort_and_search_array import search_array
from sort_and_search_array import sort_array

class MyTestCase(unittest.TestCase):
    def test_search_array_item_found(self):
        self.assertEqual(search_array(['34', '23', 3, 46], 46), 3)

    def test_search_array_item_not_found(self):
        self.assertEqual(search_array(['65', 23, -47, '12.9'], '99'), -1)


if __name__ == '__main__':
    unittest.main()
