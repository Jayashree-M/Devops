import unittest

class TestMaxFunction(unittest.TestCase):
    def test_max_with_positive_numbers(self):
        num1, num2, num3 = 10, 30, 20
        result = max(num1, num2, num3)
        self.assertEqual(result, 30)
    
    def test_max_with_negative_numbers(self):
        num1, num2, num3 = -10, -30, -20
        result = max(num1, num2, num3)
        self.assertEqual(result, -10)
    
    def test_max_with_mixed_numbers(self):
        num1, num2, num3 = -10, 30, 20
        result = max(num1, num2, num3)
        self.assertEqual(result, 30)
    
    def test_max_with_equal_numbers(self):
        num1, num2, num3 = 20, 20, 20
        result = max(num1, num2, num3)
        self.assertEqual(result, 20)
    
    def test_max_with_two_equal_max_numbers(self):
        num1, num2, num3 = 20, 30, 30
        result = max(num1, num2, num3)
        self.assertEqual(result, 30)
    
    def test_max_with_single_element(self):
        nums = [15]
        result = max(nums)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()
