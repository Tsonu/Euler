from math import sqrt
import copy
from euler import *
import datetime


def count_blocks(line_length, min_size, cache):
    solutions = 0
    if min_size > line_length:
        return solutions

    if line_length in cache:
        return cache[line_length]

    for start_pos in range(0, line_length - min_size + 1):
        solutions += 1
        solutions += count_blocks(line_length - start_pos - min_size, min_size, cache)

    if line_length not in cache:
        cache.update({line_length: solutions})
        print 'appended to cache', line_length, solutions

    return solutions

start = datetime.datetime.now()

cache = {}
red = count_blocks(50, 2, cache)
cache = {}
green = count_blocks(50, 3, cache)
cache = {}
blue = count_blocks(50, 4, cache)

print 'totals', red, green, blue, red + green + blue
print datetime.datetime.now() - start