import unittest
import sys
import os

# Add the parent directory to sys.path to import lcs
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lcs_multiline import lcs_multiline  # Assuming your function is called lcs_multiline

class TestLCSMultiline(unittest.TestCase):

    def test_lcs_multiline(self):
        lines1 = ["This is a test which contains:", "this is the lcs"]
        lines2 = ["this is the lcs", "we're testing"]
        expected = ["this is the lcs"]
        self.assertEqual(lcs_multiline(lines1, lines2), expected)

        lines1 = ["Coding Challenges helps you become a better software engineer through that build real applications.",
         "I share a weekly coding challenge aimed at helping software engineers level up their skills through deliberate practice.",
         "I've used or am using these coding challenges as exercise to learn a new programming language or technology.",
         "Each challenge will have you writing a full application or tool. Most of which will be based on real world tools and utilities."]
        lines2 = ["Helping you become a better software engineer through coding challenges that build real applications.",
         "I share a weekly coding challenge aimed at helping software engineers level up their skills through deliberate practice.",
         "These are challenges that I've used or am using as exercises to learn a new programming language or technology.",
         "Each challenge will have you writing a full application or tool. Most of which will be based on real world tools and utilities."]
        expected = ["I share a weekly coding challenge aimed at helping software engineers level up their skills through deliberate practice.",
		"Each challenge will have you writing a full application or tool. Most of which will be based on real world tools and utilities."]
        self.assertEqual(lcs_multiline(lines1, lines2), expected)

        # ABFC
        # KDBJCL
        # = BC
        lines1 = ["this is the 1st sentence , let's assume it is A", "first target , is B","this is BS","second target is C"]
        lines2 = ["cut the BS dude", "what nooo","first target , is B","testing ","second target is C","what do you know"]
        expected = ["first target , is B","second target is C"]
        self.assertEqual(lcs_multiline(lines1, lines2), expected)

        lines1 = ["", ""]
        lines2 = ["", ""]
        expected = ["",""]
        self.assertEqual(lcs_multiline(lines1, lines2), expected)

        lines1 = ["Line 1", "Line 2", "Line 3"]
        lines2 = ["Line 1", "Line 2", "Line 3"]
        expected = ["Line 1", "Line 2", "Line 3"]
        self.assertEqual(lcs_multiline(lines1, lines2), expected)

        lines1 = ["Line 1", "Line 2566", "Line 345563"]
        lines2 = ["Line 99", "Line 2", "Lin33e 3334"]
        expected = []
        self.assertEqual(lcs_multiline(lines1, lines2), expected)

        lines1 = ["Line A", "Line B", "Line C"]
        lines2 = ["Line X", "Line B", "Line Z"]
        expected = ["Line B"]
        self.assertEqual(lcs_multiline(lines1, lines2), expected)

        lines1 = ["Line A", "Line B", "Line C", "Line D"]
        lines2 = ["Line X", "Line B", "Line Y", "Line C", "Line Z"]
        expected = ["Line B", "Line C"]
        self.assertEqual(lcs_multiline(lines1, lines2), expected)


        lines1 = []
        lines2 = []
        expected = []
        self.assertEqual(lcs_multiline(lines1, lines2), expected)

        lines1 = ["Line A", "Line B"]
        lines2 = []
        expected = []
        self.assertEqual(lcs_multiline(lines1, lines2), expected)


        lines1 = ["Line A", "Line B", "Line B", "Line C"]
        lines2 = ["Line B", "Line B", "Line D"]
        expected = ["Line B", "Line B"]
        self.assertEqual(lcs_multiline(lines1, lines2), expected)


        lines1 = ["line a", "line B", "line C"]
        lines2 = ["Line A", "Line B", "Line C"]
        expected = []  # If case-sensitive
        self.assertEqual(lcs_multiline(lines1, lines2), expected)


        lines1 = ["  Line A", "Line B  ", "Line C"]
        lines2 = ["Line A", "Line B", "  Line C"]
        expected = []  # or modify the function to trim spaces and match
        self.assertEqual(lcs_multiline(lines1, lines2), expected)


        lines1 = ["Line, A!", "Line B?", "Line: C."]
        lines2 = ["Line, A!", "Different line", "Line: C."]
        expected = ["Line, A!", "Line: C."]
        self.assertEqual(lcs_multiline(lines1, lines2), expected)




if __name__ == '__main__':
    unittest.main()
