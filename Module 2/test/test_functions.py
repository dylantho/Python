import unittest
from camper_age_input import convert_to_months
#could not get "from main import camper_age_input" to work on the line above


class FunctionTestCase(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(61, convert_to_months(5))


if __name__ == '__main__':
    unittest.main()
