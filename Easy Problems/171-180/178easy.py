#https://www.reddit.com/r/dailyprogrammer/comments/2f6a7b/9012014_challenge_178_easy_transformers_matrices/

import math

def new(x, y):
	return x, y

def translate(a, b):
	return x+a, y+b

def rotate(a, b, c):
	return (round(a + math.cos(-c)*(x-a) - math.sin(-c)*(y-b), 3),
			round(b + math.sin(-c)*(x-a) + math.cos(-c)*(y-b), 3))

def scale(a, b, c):
	return a+(x-a)*c, b+(y-b)*c

def reflect(axis):
	if axis in 'Xx':
		return x, -y
	elif axis in 'Yy':
		return -x, y

X = 'X'
Y = 'Y'

print("Welcome to Matrix Transform")
print("The following commands are possible:")
print("new(x, y) \n"
	  "translate(a, b) \n"
	  "rotate(a, b, c) \n"
	  "scale(a, b, c) \n"
	  "reflect(axis) \n"
	  "finish()")
print("\n~*~----------------~*~\n")

while True:
	command = raw_input('>> ')
	if command == 'finish()':
		break
	if command.startswith('('):
		command = 'new' + command
	x, y = eval(command)
	print(x, y)