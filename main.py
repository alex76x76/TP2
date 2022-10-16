import random
import time

def read(path):
    array = [int(i) for i in open('test.txt').readline().split()]
    return array

def readmax(path):
    array = [int(i) for i in open('testmax.txt').readline().split()]
    return array

def readmin(path):
    array = [int(i) for i in open('testmin.txt').readline().split()]
    return array

def readmult(path):
    array = [int(i) for i in open('testmult.txt').readline().split()]
    return array

def readtim(path):
    array = [int(i) for i in open('testtim.txt').readline().split()]
    return array

def _min(array):
    min_ = array[0]
    for z in array:
        if z < min_:
            min_ = z
    return min_

def _max(array):
    max_ = array[0]
    for z in array:
        if z > max_:
            max_ = z
    return max_

def _mult(array):
    mul_ = 1
    for z in array:
        mul_ *= z
    return mul_

def _sum(array):
    sum_ = 0
    for z in array:
        sum_ += z
    return sum_

def get_time(size):
    test = [random.randrange(-100, 100) for z in range(size)]
    start = time.time_ns()
    _mul(test)
    return (time.time_ns() - start) / 1e6

def run_time_test():
    print(get_time(1))
    print(get_time(100000))
    print(get_time(200000))
    print(get_time(300000))
    print(get_time(400000))
    print(get_time(500000))
    print(get_time(600000))
    print(get_time(700000))
    print(get_time(800000))
    print(get_time(900000))
    print(get_time(1000000))
