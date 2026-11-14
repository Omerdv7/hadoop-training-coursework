#!/usr/bin/env python3
"""reducer_top3.py - word count, outputs only the 3 most frequent words"""
import heapq
from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    top = [] # min-heap of (count, word) pairs, holds at most 3 entries
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
        except ValueError:
            # count was not a number, so silently discard this item
            continue
        if len(top) < 3:
            heapq.heappush(top, (total_count, current_word))
        else:
            # keep only the 3 largest counts seen so far
            heapq.heappushpop(top, (total_count, current_word))
    # print in descending order of counts
    for count, word in sorted(top, reverse=True):
        print("%s%s%d" % (word, separator, count))

if __name__ == "__main__":
    main()
