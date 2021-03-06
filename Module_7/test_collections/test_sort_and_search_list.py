import unittest
from sort_and_search_list import search_list
from sort_and_search_list import sort_list


class MyTestCase(unittest.TestCase):
    def test_search_list_item_found(self):
        self.assertEqual(search_list([34, -23, '4', 12.9], '4'), 2)

    def test_search_list_item_not_found(self):
        self.assertEqual(search_list([34, -23, '4', 12.9], 25), -1)

    def test_search_list_sorted(self):
        self.assertEqual(sort_list([34, -23, 22, 12.9]), [-23, 12.9, 22, 34])



if __name__ == '__main__':
    unittest.main()
