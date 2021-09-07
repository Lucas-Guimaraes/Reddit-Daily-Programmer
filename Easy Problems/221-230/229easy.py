#https://www.reddit.com/r/dailyprogrammer/comments/3i99w8/20150824_challenge_229_easy_the_dottie_number/

#The Dottie Number

from math import cos

def dottie(x, y):
	loop_amt = 0
	while x != y:
		loop_amt += 1
		x, y = cos(x), x
	print("")
	print(x)
	print("It took {} loops to get the dottie number".format(str(loop_amt)))
	print("")

while True:
	a = raw_input("Please input a number to get the dottie number: ")
	if a.isdigit():
		dottie(int(a), None)