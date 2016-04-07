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
            assert output == "Theme \'test0\' does not exist.\nReverting to default theme."
        finally:
            sys.stdout = saved_stdout

    def testDir1(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            main.loadSpaces("test1")
            output = out.getvalue().strip()
            assert output == "Theme \'test1\' does not exist.\nReverting to default theme."
        finally:
            sys.stdout = saved_stdout

    def testDir2(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            main.loadSpaces("test2")
            output = out.getvalue().strip()
            assert output == "test2/titles.csv does not contain titles for all 40 spaces.\nReverting to default theme."
        finally:
            sys.stdout = saved_stdout

    def testDir3(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            main.loadSpaces("test3")
            output = out.getvalue().strip()
            assert output == "Theme \'test3\' does not contain image files for all 40 spaces.\nReverting to default theme."
        finally:
            sys.stdout = saved_stdout

if __name__ == '__main__':
    unittest.main()
