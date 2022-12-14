import unittest
import random
import time
from main import _sum, _mult, _min, _max, read, readmax, readmin, readmult, readtim

array = read("test.txt")
arraymax = readmax("testmax.txt")
arraymin = readmin("testmin.txt")
arraymult = readmult("testmult.txt")
arraytim = readtim("testtim.txt")

class utest(unittest.TestCase):
    
    def test_min(self):
        self.assertTrue(_min(array) == -9)
        self.assertTrue(_min(arraymin) == -7)
        self.assertTrue(_min(arraymax) == -3)
        self.assertTrue(_min(arraymult) == -3000)
        self.assertTrue(_min(arraytim) == -3000)

    def test_max(self):
        self.assertTrue(_max(array) == 9)
        self.assertTrue(_max(arraymin) == 7)
        self.assertTrue(_max(arraymax) == 3)
        self.assertTrue(_max(arraymult) == 3000)
        self.assertTrue(_max(arraytim) == 3000)
    
    def test_sum(self):
        self.assertTrue(_sum(array) == 20)
        self.assertTrue(_sum(arraymin) == -0)
        self.assertTrue(_sum(arraymax) == 0)
        self.assertTrue(_sum(arraymult) == 16267)
        self.assertTrue(_sum(arraytim) == -297327)

    def test_mult(self):
        self.assertTrue(_mult(array) == 14932726824960)
        self.assertTrue(_mult(arraymin) == 0)
        self.assertTrue(_mult(arraymax) == 0)
        self.assertTrue(_mult(arraymult) == 0)
        self.assertTrue(_mult(arraytim) == 0)
        
    def test_sum_int(self):
        self.assertIsInstance(_sum(array), int)
        
if __name__ == "__main__":
    unittest.main()
