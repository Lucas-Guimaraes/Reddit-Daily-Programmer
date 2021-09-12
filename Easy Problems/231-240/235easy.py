#https://www.reddit.com/r/dailyprogrammer/comments/3nkanm/20151005_challenge_235_easy_ruthaaron_pairs/

#Creates Distinct Prime Factor List
def prime_factor_list(n):
	prime_list = []
	#Returns if 2 or below. If not, append 2.
	if n <= 2:
		return prime_list
	if n % 2 == 0:
		prime_list.append(2)

	#Checks range
	for i in range(3, n):
		isPrime = True
		#If its not even
		if i % 2 != 0:

			#If it doesnt divide into our main number (N)
			if n % i != 0:
				isPrime = False
				continue

			#If it divides into any pre-existing prime
			for p in prime_list:
				if i % p == 0:
					isPrime = False
					break

			#If none of the prime checks were broken
			if isPrime:
				prime_list.append(i)

	#Return
	return prime_list

#Function that gets primes of A and B
def ruth_aaron_pairs(a, b):
	a_lst = prime_factor_list(a)
	b_lst = prime_factor_list(b)
	tup = "({}, {}) ".format(a, b)
	return tup + "VALID" if sum(a_lst) == sum(b_lst) else tup + "NOT VALID"


#Introductory text
print("Welcome to Ruth Aaron Pairs")
print("Input two numbers, and this program will tell you whether they are a ruth aaron pair!")
print("\n~*~----------------~*~\n")

#Looping
ruth = True

while ruth:
	n = raw_input("First Digit: ")
	m = raw_input("Second Digit: ")
	#Checks quit code
	if n.lower() == "q" or m.lower == "q":
		break

		#Type check
	if n.isdigit() and m.isdigit():
		print("")
		print(ruth_aaron_pairs(int(n), int(m)))
		print("")

raw_input("\nPress enter to exit.")

#Test Case
#print(ruth_aaron_pairs(714, 715))