import unittest
from Student import Student


class MyTestCase(unittest.TestCase):
    # Test 1: Required parameters Status: Pass
    def setUp(self):
        self.student = Student('Oliver', 'John', 'Media')

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Oliver')
        self.assertEqual(self.student.first_name, 'John')
        self.assertEqual(self.student.major, 'Media')

    def tearDown(self):
        del self.student

    # Test 2: Required parameters Status: Pass
    def setUp(self):
        self.student = Student('Oliver', 'John', 'Media', 3.8)

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.last_name, 'Oliver')
        self.assertEqual(self.student.first_name, 'John')
        self.assertEqual(self.student.major, 'Media')
        self.assertEqual(self.student.gpa, 3.8)

    def tearDown(self):
        del self.student


if __name__ == '__main__':
    unittest.main()
