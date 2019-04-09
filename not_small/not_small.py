#!/usr/bin/env python3
import sys

fname = sys.argv[1]

lines = open(fname).read().split('\n')
last = len(lines)
high = 0
for i in lines:
	last = last - 1
	if float(i)  > high:
		high = float(i)
	if last == 0:
		sys.stdout.write(str(int(high)))