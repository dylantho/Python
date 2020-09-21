import unittest
from coupon_calculations import calculate_price


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        #(example) self.assertAlmostEqual(calculate_price(cost, cash off, percent off),"expected result here", places=4)
        self.assertAlmostEqual(calculate_price(4.0, 5.0, 0.1), 4.996, places=2)
        self.assertAlmostEqual(calculate_price(6.0, 5.0, 0.15), 6.851, places=2)
        self.assertAlmostEqual(calculate_price(8.24, 5.0, 0.2), 8.697, places=2)
        self.assertAlmostEqual(calculate_price(6.45, 10.0, 0.1), 2.563, places=2)
        self.assertAlmostEqual(calculate_price(7.85, 10.0, 0.15), 4.013, places=2)
        self.assertAlmostEqual(calculate_price(9.24, 10.0, 0.2), 5.306, places=2)
    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(calculate_price(11.25, 5.0, 0.1), ???, places=2)
        self.assertAlmostEqual(calculate_price(22.0, 5.0, 0.15), ???, places=2)
        self.assertAlmostEqual(calculate_price(28.33, 5.0, 0.2), ???, places=2)
        self.assertAlmostEqual(calculate_price(14.24, 10.0, 0.1), ???, places=2)
        self.assertAlmostEqual(calculate_price(21.40, 10.0, 0.15), ???, places=2)
        self.assertAlmostEqual(calculate_price(29.21, 10.0, 0.2), ???, places=2)








if __name__ == '__main__':
    unittest.main()
