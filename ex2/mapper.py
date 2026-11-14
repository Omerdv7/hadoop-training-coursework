#!/usr/bin/env python3
"""mapper.py - word count with cleaning:
1. strip trailing commas and dots from each word
2. case-insensitive (everything lowercase)"""
import sys

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            # remove trailing commas/dots and lowercase the word
            word = word.rstrip(',.').lower()
            # skip words that became empty (e.g. a lone "," or ".")
            if word:
                print('%s%s%d' % (word, separator, 1))

if __name__ == "__main__":
    main()
