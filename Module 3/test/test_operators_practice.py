import unittest

class OperatorsTest(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(5 == 5)
        #initial test instructed to fix

    def test_equal_operator(self):
        a = 7
        b = 7
        self.assertTrue(a == b)

    def test_notequal_operator(self):
        a = 6
        b = 5
        self.assertTrue(a != b)

    def test_greater_operator(self):
        a = 5
        b = 2
        self.assertTrue(a > b)

    def test_less_operator(self):
        a = 1
        b = 2
        self.assertTrue(a < b)

    def test_greater_or_operator(self):
        a = 4
        b = 4
        self.assertTrue(a >= b)

    def test_less_or_operator(self):
        a = 3
        b = 5
        self.assertTrue(a <= b)

if __name__ == '__main__':
    unittest.main()
