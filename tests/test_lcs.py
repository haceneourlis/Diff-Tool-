import unittest
import sys
import os

# Add the parent directory to sys.path to import lcs
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lcs import lcs

class TestLCS(unittest.TestCase):

    def test_lcs(self):
        # Test case 1: Basic example
        X = "AGGTAB"
        Y = "GXTXAYB"
        expected = "GTAB"
        self.assertEqual(lcs(X, Y), expected)
        
        # Test case 2: One string is a subsequence of the other
        X = "AABCXY"
        Y = "XYZ"
        expected = "XY"
        self.assertEqual(lcs(X, Y), expected)
        
        # Test case 3: Common subsequence at the start
        X = "ABCD"
        Y = "AC"
        expected = "AC"
        self.assertEqual(lcs(X, Y), expected)
        
        # Test case 4: No common subsequence
        X = "ABCDE"
        Y = "XYZ"
        expected = ""
        self.assertEqual(lcs(X, Y), expected)
        
        # Test case 5: Identical strings
        X = "IDENTICAL"
        Y = "IDENTICAL"
        expected = "IDENTICAL"
        self.assertEqual(lcs(X, Y), expected)
        
        # # Test case 6: Strings with different cases
        # X = "CaseSensitive"
        # Y = "casesensitive"
        # expected = "casesensitive"  # Assuming case-insensitive comparison
        # self.assertEqual(lcs(X, Y), expected)
        
        # Test case 7: Empty strings
        X = ""
        Y = ""
        expected = ""
        self.assertEqual(lcs(X, Y), expected)
        
        # Test case 8: Empty string with non-empty string
        X = ""
        Y = "NonEmpty"
        expected = ""
        self.assertEqual(lcs(X, Y), expected)
        
        X = "NonEmpty"
        Y = ""
        expected = ""
        self.assertEqual(lcs(X, Y), expected)
        
        # Test case 9: Strings with special characters
        X = "Line@1!"
        Y = "Line@1!"
        expected = "Line@1!"
        self.assertEqual(lcs(X, Y), expected)
        
        # Test case 10: Strings with numbers
        X = "12345"
        Y = "135"
        expected = "135"
        self.assertEqual(lcs(X, Y), expected)
        
        # Test case 11: Long strings with simple LCS
        X = "A" * 1000 + "B" * 1000
        Y = "A" * 500 + "B" * 500
        expected = "A" * 500 + "B" * 500
        self.assertEqual(lcs(X, Y), expected)

if __name__ == '__main__':
    unittest.main()
