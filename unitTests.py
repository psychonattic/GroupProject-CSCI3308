import unittest
import sys
from StringIO import StringIO
import main

class ModopolyTestCase(unittest.TestCase):

    def testDir0(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            main.loadSpaces("test0")
            output = out.getvalue().strip()
            assert output == "Path to theme \'test0\' does not exist or test0/spaces.csv does not exist.\nAttempting to load default theme." 
        finally:
            sys.stdout = saved_stdout

    def testDir1(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            main.loadSpaces("test1")
            output = out.getvalue().strip()
            assert output == "Path to theme \'test1\' does not exist or test1/spaces.csv does not exist.\nAttempting to load default theme."
        finally:
            sys.stdout = saved_stdout

    def testDir2(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            main.loadSpaces("test2")
            output = out.getvalue().strip()
            assert output == "Theme \'test2\' does not contain image files for all 40 spaces.\nAttempting to load default theme."
        finally:
            sys.stdout = saved_stdout

    #Tests for missing titles (line 1 of spaces.csv)
    def testDir3_1(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            main.loadSpaces("test3_1")
            output = out.getvalue().strip()
            assert output == "test3_1/spaces.csv does not contain titles and/or types for all 40 spaces.\nAttempting to load default theme."
        finally:
            sys.stdout = saved_stdout
    #Tests for missing types (line 2 of spaces.csv)
    def testDir3_2(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            main.loadSpaces("test3_2")
            output = out.getvalue().strip()
            assert output == "test3_2/spaces.csv does not contain titles and/or types for all 40 spaces.\nAttempting to load default theme."
        finally:
            sys.stdout = saved_stdout

    #Tests for missing prices (line 3 of spaces.csv)
    def testDir4_1(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            main.loadSpaces("test4_1")
            output = out.getvalue().strip()
            assert output == "Number of given prices and/or rent does not match number of purchasable spaces.\nAttempting to load default theme."
        finally:
            sys.stdout = saved_stdout
    #Tests for missing rent (line 4 of spaces.csv)
    def testDir4_2(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            main.loadSpaces("test4_2")
            output = out.getvalue().strip()
            assert output == "Number of given prices and/or rent does not match number of purchasable spaces.\nAttempting to load default theme."
        finally:
            sys.stdout = saved_stdout

    #Tests for missing housing costs (line 5 of spaces.csv)
    def testDir5_1(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            main.loadSpaces("test5_1")
            output = out.getvalue().strip()
            assert output == "Number of house costs and/or colors does not match number of property spaces.\nAttempting to load default theme."
        finally:
            sys.stdout = saved_stdout
    #Tests for missing colors (line 6 of spaces.csv)
    def testDir5_2(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            main.loadSpaces("test5_2")
            output = out.getvalue().strip()
            assert output == "Number of house costs and/or colors does not match number of property spaces.\nAttempting to load default theme."
        finally:
            sys.stdout = saved_stdout

if __name__ == '__main__':
    unittest.main()
