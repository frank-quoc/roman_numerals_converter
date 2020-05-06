import unittest
from unittest.mock import patch

from roman_numerals import RomanNumeral

class TestRomanNumerals(unittest.TestCase): #sublcass of test case class
    """A test class for our Roman numerals."""
    
    @patch('builtins.input', return_value="DLXII")
    def test_roman_to_int(self, mock_input):
        result = RomanNumeral("DLXII").roman_to_int()
        self.assertEqual(result, 562)
