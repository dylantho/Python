import unittest
from dict_membership import in_dict


class MyTestCase(unittest.TestCase):

    """Test expect true"""
    def test_in_dict(self):
        self.assertEqual(in_dict({'A': 3, 'B': 4, 'C': 5}, 'B'), True)

    """"Test expect false"""
    def test_in_dict(self):
        self.assertEqual(in_dict({'A': 3, 'B': 4, 'C': 5}, 'D'), False)


if __name__ == '__main__':
    unittest.main()

