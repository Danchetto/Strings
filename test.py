import unittest
from main import main_script


class Test(unittest.TestCase):

    def test_001(self):
        dat = "tests/001.dat"
        ans = "tests/001.ans"
        main_script(dat, 'output.txt')
        self.assertEqual(open(ans).read(), open('output.txt').read())

    def test_002(self):
        dat = "tests/002.dat"
        ans = "tests/002.ans"
        main_script(dat, 'output.txt')
        self.assertEqual(open(ans).read(), open('output.txt').read())

    def test_003(self):
        dat = "tests/003.dat"
        ans = "tests/003.ans"
        main_script(dat, 'output.txt')
        self.assertEqual(open(ans).read(), open('output.txt').read())

    def test_004(self):
        dat = "tests/004.dat"
        ans = "tests/004.ans"
        main_script(dat, 'output.txt')
        self.assertEqual(open(ans).read(), open('output.txt').read())

    def test_005(self):
        dat = "tests/005.dat"
        ans = "tests/005.ans"
        main_script(dat, 'output.txt')
        self.assertEqual(open(ans).read(), open('output.txt').read())

    def test_006(self):
        dat = "tests/006.dat"
        ans = "tests/006.ans"
        main_script(dat, 'output.txt')
        self.assertEqual(open(ans).read(), open('output.txt').read())

    def test_007(self):
        dat = "tests/007.dat"
        ans = "tests/007.ans"
        main_script(dat, 'output.txt')
        self.assertEqual(open(ans).read(), open('output.txt').read())