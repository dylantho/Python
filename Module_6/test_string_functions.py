import unittest
from string_functions import multiply_string

class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(multiply_string("Dylan", 8), "DylanDylanDylanDylanDylanDylanDylanDylan")


if __name__ == '__main__':
    unittest.main()
