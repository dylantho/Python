import unittest
import unittest.mock as mock
from average_scores import average


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[89, 80, 98]):
            assert average() == 89



if __name__ == '__main__':
    unittest.main()
