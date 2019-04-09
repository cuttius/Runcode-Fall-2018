#!/usr/bin/env python3
import sys

fname = sys.argv[1]
rstart = sys.argv[2]
rend = sys.argv[3]

def sortSecond(val):
	return val[1]

def substring_after(s, delim):
	return s.partition(delim)[2]

def substring_before(s, delim):
	return s.partition(delim)[0]

lines = open(fname).read().split('\n')
last_line = len(lines)
salary_list = []

for idx, val in enumerate(lines):
	if val != '':
		salary_list.append([substring_before(val, "$"), int(substring_after(val, "$"))])


salary_list.pop()

salary_list.sort(key=sortSecond)

last = len(salary_list)

for i, val in enumerate(salary_list):
	last = last - 1
	if val[1] >= int(rstart) and val[1] <= int(rend):
		sys.stdout.write(val[0] + "$" + str(val[1]))
		if last > 0:
			sys.stdout.write("\n")
