import unittest
from main import camper_age_input


class FunctionTestCase(unittest.TestCase):
    def convert_to_months(self):
        self.assertEqual(60, camper_age_input.years(5))


if __name__ == '__main__':
    unittest.main()
