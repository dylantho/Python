import unittest
from camper_age_input import convert_to_months

class FunctionTestCase(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(60, convert_to_months(5))


if __name__ == '__main__':
    unittest.main()
