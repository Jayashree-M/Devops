import unittest

class TestMaxFunction(unittest.TestCase):
    def test_max(self):
        num1, num2, num3 = 10, 30, 20
        result = max(num1, num2, num3)
        self.assertEqual(result, 30)

if __name__ == '__main__':
    unittest.main()
