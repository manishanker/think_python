#!/usr/bin/env python

import sys

#fucntion to print the string at column 70 of screen

def print_at_70(s):
	if not s:
		print "String is empty, send a valid string!"
	else:
		return ' '*70 + s 


if __name__=='__main__':
	if len(sys.argv) != 2:
		print "Usage: python ex_3_4.py allen"
	else:
		result=print_at_70(sys.argv[1])
		print result
