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

    # Test 3: __str__ Status: Pass
    def setUp(self):
        self.student = Student('Oliver', 'John', 'Media', 3.8)

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Oliver, John has major Media with gpa: 3.8')

    def tearDown(self):
        del self.student

    # Test 4: Invalid last_name Status: Pass
    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = Student('123', 'John', 'Media')

    # Test 5: Invalid first_name Status: Pass
    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            p = Student('Oliver', '123', 'Media')

    # Test 6: Invalid Major Status: Pass
    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = Student('Oliver', 'John', '123')

    # Test 7: Invalid gpa (non numeric) Status: Pass
    def test_object_not_created_error_gpa(self):
        with self.assertRaises(AttributeError):
            p = Student('Oliver', 'John', 'Media', 'twenty')

    # Test 8: Invalid gpa (outside of range) Status: Fail
    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            p = Student('Oliver', 'John', 'Media', 5.0)












if __name__ == '__main__':
    unittest.main()
