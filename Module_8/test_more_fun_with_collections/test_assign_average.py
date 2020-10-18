import unittest
from assign_average import switch_average


class MyTestCase(unittest.TestCase):

    def test_switch_average_A(self):
        self.assertEqual(switch_average('A'), 97)

    def test_switch_average_B(self):
        self.assertEqual(switch_average('B'), 87)

    def test_switch_average_C(self):
        self.assertEqual(switch_average('C'), 75)

    def test_switch_average_D(self):
        self.assertEqual(switch_average('D'), 68)

    def test_switch_average_E(self):
        self.assertEqual(switch_average('E'), 55)

    def test_switch_average_non_key(self):
        self.assertEqual(switch_average('Z'), "Invalid key")


if __name__ == '__main__':
    unittest.main()
