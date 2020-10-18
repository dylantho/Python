import unittest
from set_membership import in_set

class MyTestCase(unittest.TestCase):

    """Test expect true"""
    def test_in_set(self):
        self.assertEqual(in_set({3, 4, 5}, 4), True)

    """"Test expect false"""
    def test_in_set(self):
        self.assertEqual(in_set({3, 4, 5}, 6), False)


if __name__ == '__main__':
    unittest.main()
