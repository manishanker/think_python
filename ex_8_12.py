#!/usr/bin/env python

def rotate(s, i):
	"""
		s is the string, i is the integer by which the character of
		s has to be shifted.
	"""	
	#print s,i
	if (s is not None) and (i is not None):
		print ''.join(map((lambda k : chr(ord(k) + i )), s))
		return ''.join(map((lambda k : chr(ord(k) + i )), s))
	else:	
		print "string or integer to shift missing."


if __name__=='__main__':
	#rotate()
	#rotate(s='mani')
	rotate(s='cheer',i= 7)
	rotate(s='melon',i= -10)
