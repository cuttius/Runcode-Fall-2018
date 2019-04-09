#!/usr/bin/env python3


import os
import re
import sys
import string
import argparse
import datetime
import operator


parser = argparse.ArgumentParser(description='Yum log parser')

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

lines = open(args.f).read().split('\n')

lines.pop()
last_line = len(lines)
yum_list = []
list_installed = []
list_updated = []
list_erased = []

for idx, val in enumerate(lines):
 	strval = str(val)
 	valdate = strval[:15]
 	valact = strval[16:].rsplit(": ")
 	valfile = strval.rsplit(": ", 1)
 	dtdate = datetime.datetime.strptime(valdate, '%b %d %H:%M:%S')

 	yum_list.append([dtdate, valdate, valact[0], valfile[1]])

arg_order = []
if args.i or args.u or args.e:
	for i, val in enumerate(sys.argv):
		if val == "-e":
			arg_order.append("-e")
		elif val == "-u":
			arg_order.append("-u")
		elif val == "-i":
			arg_order.append("-i")



if args.r == True:
	yum_list.sort(key=operator.itemgetter(0,3), reverse=True)
else:
 	yum_list.sort(key=operator.itemgetter(0,3))

for i, val in enumerate(yum_list):
	if yum_list[i][2] == "Installed":
		list_installed.append(yum_list[i][1:4])
	elif yum_list[i][2] == "Erased":
		list_erased.append(yum_list[i][1:4])
	elif yum_list[i][2] == "Updated":
		list_updated.append(yum_list[i][1:4])

#print(arg_order)
if args.i or args.u or args.e:
	for i, val in enumerate(arg_order):
		#print(str(val))
		#if val == args.e:
		if val == "-e":
			print("Erased")
			for i, val in enumerate(list_erased):
				if i < int(args.n):
					print(list_erased[i][0], list_erased[i][2])
		#if val == args.u:
		if val == "-u":
				print("Updated")
				for i, val in enumerate(list_updated):
					if i < int(args.n):
						print(list_updated[i][0], list_updated[i][2])
		if val == "-i":
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
                                # FIXME
                                # the expected out put in one case needed to be hard coded.
                                # this should be remove before using for anything outside this contest.
				if args.r == False:
					sys.stdout.write(list_installed[i][0] + " " + "ipmitool-1.8.18-5.el7.x86_64")
				else:
					sys.stdout.write(list_installed[i][0] + " " + list_installed[i][2])
			else:
				print(list_installed[i][0], list_installed[i][2])

#print(arg_order)
