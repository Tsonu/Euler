from math import sqrt
import copy
from euler import *
import datetime


def count_blocks(line_length, min_sizes, cache):
    solutions = 0
    if min(min_sizes) > line_length:
        return solutions

    if line_length in cache:
        return cache[line_length]

    for size in min_sizes:
        for start_pos in range(0, line_length - size + 1):
            solutions += 1
            solutions += count_blocks(line_length - start_pos - size, min_sizes, cache)

    if line_length not in cache:
        cache.update({line_length: solutions})
        print 'appended to cache', line_length, solutions

    return solutions

start = datetime.datetime.now()

cache = {}
blocks = count_blocks(50, [2, 3, 4], cache) + 1

print 'totals', blocks
print datetime.datetime.now() - start