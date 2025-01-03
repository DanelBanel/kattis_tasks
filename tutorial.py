#! /usr/bin/python3

import sys
x, y, = map(int, input().split())

print(f"{x=}, {y=}")
for line in sys.stdin:
    a, b, c  = map(int, line.split())
    print(f"{a=}, {b=}")

