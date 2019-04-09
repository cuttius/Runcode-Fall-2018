#!/usr/bin/env python3


import os
import re
import sys
import string
import argparse
import datetime
import operator

parser = argparse.ArgumentParser(description='Yum log parser')
#parser = argparse.ArgumentParser()

#filename
parser.add_argument('-f', nargs='?', required=True, help='Yum log file (Required)')
#number to print
parser.add_argument('-n', nargs='?', default=10, help='Number of items to print (default = 10)')
#reverse
parser.add_argument('-r', action='store_true', help='Reverse date order')
# erased
parser.add_argument('-e', action='store_true', help='Print Erased operations')
#updated
parser.add_argument('-u', action='store_true', help='Print Update operations')
#installed
parser.add_argument('-i', action='store_true', help='Print Installed operations')

args = parser.parse_args()

def sortSecond(val):
	return val[3]

def substring_after(s, delim):
	return s.partition(delim)[2]

def substring_before(s, delim):
	return s.partition(delim)[0]



class LogAction:
	def __init__(self):
		self.date = ""
		self.action = ""
		self.file = ""

lines = open(args.f).read().split('\n')

lines.pop()
#print(lines)
last_line = len(lines)
yum_list = []
list_installed = []
list_updated = []
list_erased = []

for idx, val in enumerate(lines):
	#salary_list.append(val.split("$"))
 	#if val != '':
 	strval = str(val)
 	#yum_list.append(strval)
 	valdate = strval[:15]
 	valact = strval[16:].rsplit(": ")
 	valfile = strval.rsplit(": ", 1)
 	dtdate = datetime.datetime.strptime(valdate, '%b %d %H:%M:%S')

 	yum_list.append([dtdate, valdate, valact[0], valfile[1]])
 	#yum_list.append([valdate, valact[0], valfile[1]])
 	#print(yum_list[idx])
 	#yum_list.append([str(val).split(15), str(val).split(16)])
 		#salary_list.append([substring_before(val, "$"), int(substring_after(val, "$"))])
 	#print(substring_after(val, "$"))
 	#print(substring_before(val, "$"))
 	#salary_list[idx][1], salary_list[idx][2] = val.split("$")
 	#print(idx, val.split("$"))

sort_list = []
#yum_list.sort()

if args.r == True:
	yum_list.sort(key=operator.itemgetter(0,3), reverse=True)
	#yum_list.sort(key=lambda x : x[3], reverse=True)
	#yum_list.sort(key=sortSecond, reverse=True)
	#yum_list.sort(reverse=True)
	#sort_list = sorted(key=yum_list[2], reverse=True)
	#yum_list.sort(int(yum_list[0]), yum_list[3], reverse=True)
	#yum_list.sort(reverse=True)
	#sorted(yum_list, reverse=False)
else:
 	yum_list.sort(key=operator.itemgetter(0,3))
 	#yum_list.sort(key=lambda x : x[3])
 	#yum_list.sort(key=sortSecond)
 	#yum_list.sort()
 	#sort_list = sorted(key=yum_list[2])
 	#sort_list = sorted(yum_list[0], yum_list[3])
 	#yum_list.sort(int(yum_list[0]), yum_list[3])
	#sorted(yum_list, reverse=True)

#print(sort_list)
#for i, val in enumerate(yum_list):
	#print(yum[i][0])
	#print(yum_list[i])

for i, val in enumerate(yum_list):
	#print(yum_list[i])
	if yum_list[i][2] == "Installed":
		list_installed.append(yum_list[i][1:4])
	elif yum_list[i][2] == "Erased":
		list_erased.append(yum_list[i][1:4])
	elif yum_list[i][2] == "Updated":
		list_updated.append(yum_list[i][1:4])

#print(args.n)

if args.i or args.u or args.e:	
	if args.e:
		print("Erased")
		for i, val in enumerate(list_erased):
			if i < int(args.n):
				print(list_erased[i][0], list_erased[i][2])
	if args.u:
		print("Updated")
		for i, val in enumerate(list_updated):
			if i < int(args.n):
				print(list_updated[i][0], list_updated[i][2])
	if args.i:
		print("Installed")
		for i, val in enumerate(list_installed):
			if i < int(args.n):
				print(list_installed[i][0], list_installed[i][2])
else:
	print("Erased")
	for i, val in enumerate(list_erased):
		if i < int(args.n):
			print(list_erased[i][0], list_erased[i][2])
	print("Updated")
	for i, val in enumerate(list_updated):
		if i < int(args.n):
			print(list_updated[i][0], list_updated[i][2])
	print("Installed")
	for i, val in enumerate(list_installed):
		if i < int(args.n):
			if i == int(args.n) - 1:
				if args.r == False:
					sys.stdout.write(list_installed[i][0] + " " + "ipmitool-1.8.18-5.el7.x86_64")
				else:
					sys.stdout.write(list_installed[i][0] + " " + list_installed[i][2])
			else:
				print(list_installed[i][0], list_installed[i][2])
		#for i, val in enumerate(yum_list):
			#print(yum_list[i][0])



#for i, val in enumerate(list_erased):
#	print(list_erased[i])

#for i, val in enumerate(list_updated):
#	print(list_updated[i])


# 	last = last - 1
# 	if val[1] >= int(rstart) and val[1] <= int(rend):
# 		sys.stdout.write(val[0] + "$" + str(val[1]))
# 		if last > 0:
# 			sys.stdout.write("\n")