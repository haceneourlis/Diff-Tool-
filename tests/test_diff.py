import unittest
import sys
import os

# Add the parent directory to sys.path to import lcs
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from diff import diff
class TestGenerateDiff(unittest.TestCase):
    
    def test_diff(self):
        lines1 = [
            "Line 1",
            "Line 2",
            "Line 3"
        ]
        lines2 = [
            "Line 2",
            "Line 3",
            "Line 4"
        ]
        expected = [
            "< Line 1",
            "> Line 4"
        ]
        self.assertEqual(diff(lines1, lines2), expected)
        
        # Edge Case: Empty Arrays
        lines1 = []
        lines2 = []
        expected = []
        self.assertEqual(diff(lines1, lines2), expected)
        
        # Case with No Differences
        lines1 = [
            "Same Line 1",
            "Same Line 2"
        ]
        lines2 = [
            "Same Line 1",
            "Same Line 2"
        ]
        expected = []
        self.assertEqual(diff(lines1, lines2), expected)
        
        # Case with All Unique Lines
        lines1 = [
            "Unique 1",
            "Unique 2"
        ]
        lines2 = [
            "Unique 3",
            "Unique 4"
        ]
        expected = [
            "< Unique 1",
            "< Unique 2",
            "> Unique 3",
            "> Unique 4"
        ]
        self.assertEqual(diff(lines1, lines2), expected)

         # Edge Case: separeted by LCS lines !
        lines1 = [
                "X*",
                "if you do not do what I say",
                "you will be panished" ,
                "this is a separator , believe it or not",
                "severely"]
        lines2 = [
                "1",
                "if you do not do what I say",
                "you will not be panished actaully , i love u",
                "this is a separator , believe it or not",
                "severely ; sike I dont"]
        expected = [
                "< X*",
                "> 1",
                "< you will be panished",
                "> you will not be panished actaully , i love u",
                "< severely",
                "> severely ; sike I dont"]
        self.assertEqual(diff(lines1, lines2), expected)
if __name__ == '__main__':
    unittest.main()
