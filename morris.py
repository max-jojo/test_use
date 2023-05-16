#!/usr/bin/env python3

import sys
from random import random

NCTRS = 5

def main():

    nitems = int(sys.argv[1])
    counter = [0]*NCTRS
    for i in range(nitems):
        for c in range(NCTRS):
            if random() < 1/2**counter[c]:
                counter[c] += 1

    avg = sum([2**c for c in counter]) / NCTRS
    print(avg)


if __name__ == "__main__":
    main()
