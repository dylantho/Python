import unittest
from coupon_calculations import calculate_price


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        #(example) self.assertAlmostEqual(calculate_price(cost, cash off, percent off),"expected result here", places=4)
        self.assertAlmostEqual(calculate_price(4.0, 5.0, .1), 5.95, places=4)
        self.assertAlmostEqual(calculate_price(6.0, 5.0, .15), 6.851, places=4)
        self.assertAlmostEqual(calculate_price(8.24, 5.0, .2), 9.838, places=4)
        self.assertAlmostEqual(calculate_price(6.45, 10.0, .1), 2.045, places=4)
        self.assertAlmostEqual(calculate_price(7.85, 10.0, .15), 3.4775, places=4)
        self.assertAlmostEqual(calculate_price(9.24, 10.0, .2), 5.038, places=4)









if __name__ == '__main__':
    unittest.main()
