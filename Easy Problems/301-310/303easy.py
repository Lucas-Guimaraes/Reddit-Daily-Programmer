#https://www.reddit.com/r/dailyprogrammer/comments/5vb1wf/20170221_challenge_303_easy_ricochet/

#Finds the greatest common divisor
def gcd(a, b):
	c = 0
	while a != 0:
		c = a
		a = b % a
		b = c
	return b

#Finds the lowest common multiplier
def lcm(a, b):
	return a * b / gcd(a, b);

#^ handles finding C.

def ricochet(w, h, v):
	t = lcm(w, h) / v #finds the time it took for the particle to reach C
	b = t * v / w + t * v / h - 2; #finds the amount of time it ricochets
	ud = "UL"[t * v / h % 2];
	lr = "RL"[t * v / w % 2];
	return "{}{} {} {}".format(ud, lr, b, t)

print(ricochet(8, 3, 1))
print(ricochet(15, 4, 2))