import unittest
from if_elif_assignment import tellPrice

class MyTestCase(unittest.TestCase):
    def test_tellPrice(self):
        #Test Platinum expecting to return 1 meaning the first plan - passed
        self.assertEqual(1, tellPrice("Platinum"))

        #Test Gold expecting to return 2 meaning the second plan - passed
        self.assertEqual(2, tellPrice("Gold"))

        #Test lowercase gold expecting to still return 2 meaning the second plan - passed
        self.assertEqual(2, tellPrice("gold"))

        #Test random word to see if it returns 6 as it should - passed
        self.assertEqual(6, tellPrice("Whoops"))

        #Test Gold expecting to return 3 and fail - failed
        self.assertEqual(3, tellPrice("Gold"))



if __name__ == '__main__':
    unittest.main()
