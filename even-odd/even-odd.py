#!/usr/bin/env python3
import sys

# print true for even and false for odd.

fname = sys.argv[1]

lines = open(fname).read().split('\n')
last = len(lines)

for i in lines:
	last = last - 1
	if int(i) % 2 == 0:
		sys.stdout.write(i + " True")
	else:
		sys.stdout.write(i + " False")
	if last > 0:
		sys.stdout.write("\n")