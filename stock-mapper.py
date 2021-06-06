#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) >=2:
        open = line[1]
        high = line[2]
        low = line[3]
        close = line[4]
        volume = line[6]
        company = line[7]
        print('{}\t{}\t{}\t{}\t{}\t{}'.format(open, high, low, close, volume, company))