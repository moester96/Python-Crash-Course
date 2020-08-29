import unittest
from full_name_function import format_name


class TestCase(unittest.TestCase):
    def test_full_name(self):
        formatted_name = format_name(('tom', 'jerry'))
        self.assertEqual(formatted_name, 'Tom Jerry')

    def test_middle_name(self):
        formatted_name = format_name(('how', 'you'), 'are')
        self.assertEqual(formatted_name, 'How Are You')


if __name__ == '__main__':
    unittest.main()
