#!/usr/bin/env python2.7

def challenge_1():
	string = raw_input('string: ')
	print string[0]+string[:-len(string):-1]

def challenge_2():
	string = raw_input('string: ')
	final_string = []
	for x in range(len(string)):
		final_string.append(ord(string[x]))
	print final_string
	print sum(final_string)

def challenge_4():
	from math import sqrt, trunc
	def pythag(base, height):
		return sqrt((base**2)+(height**2))
	side = float(raw_input('side len: '))
	hside = (.5*side)
	a_path = pythag(side, hside)
	b_path = pythag(side, hside)
	print trunc((a_path+b_path))
	
def challenge_5(listofstrings = None):
	lines = []
	if listofstrings is None:	
		for x in range(5):
			lines.append(raw_input('input: '))
	answers = []
	for i in range(5):
		for x in range(50):
			if lines[i][x] == '@':
				answers.append('{0}-{1}'.format(i+1, x))
			else:
				pass
	for x in range(len(answers)):
		if x < (len(answers)-1):
			print '{}, '.format(answers[x]),
		else:
			print '{}'.format(answers[x])

if __name__ == '__main__':
	challenge_5()
