#!/usr/bin/env python3
import sys
import os
from os import walk
from os.path import join
import hashlib

"""
This challenge wanted me to hash all the files in a directory, then
hash to directory.
"""

def sha1(fname):
    hash_sha1 = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha1.update(chunk)
    return hash_sha1.hexdigest()

chall_dir = sys.argv[1]
real = []

for(root, dirs, files) in os.walk(chall_dir):
	for name in files:
		real.append([name, sha1(os.path.abspath(os.path.join(root, name)))])
real.sort()

final = ""
for i, val in enumerate(real):
	final = final + val[1]

h_sha1 = hashlib.sha1()
final = ""
for i, val in enumerate(real):
	final = final + val[1]

h_sha1.update(final.encode())
final_hash = h_sha1.hexdigest()

sys.stdout.write(h_sha1.hexdigest())