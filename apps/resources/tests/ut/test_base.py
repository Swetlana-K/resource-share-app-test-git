from django.test import TestCase

class TestBasicCalculation(TestCase):
    # Unittest
    def test_basic_sum(self):
        # Arrange
        x = 1
        y = 4
        expected_output = 5
        
        # Act
        
        result = x+y
    
        # assert
        # assert result == expected_output
        self.assertEqual(result, expected_output)
    