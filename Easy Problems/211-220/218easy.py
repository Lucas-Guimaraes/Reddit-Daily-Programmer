#https://www.reddit.com/r/dailyprogrammer/comments/38yy9s/20150608_challenge_218_easy_making_numbers/

#Runs palindrome code
def num_palindromic(n):
	steps = 0
	new = str(n)
	while not_palindrome(new):
		steps += 1
		new = str(int(new) + int(new[::-1]))
	#prints
	return "{} gets palindromic after {} steps: {}".format(str(n), steps, new)

#Checks if a palindrome/we can break out of while loop
def not_palindrome(n):
	if n != n[::-1]:
		return True
	else:
		return False

# Input
print("Welcome to palindromic numbers!")
print("Please put your number:")
print("\n~*~----------------~*~\n")

# Run code
pal = True
while pal:
	i = raw_input()
	if i.lower() == 'q':
		break
	if i.isdigit():
		print(num_palindromic(int(i)))


print("Press enter to exit")

#Test Cases
#print(num_palindromic(123))
#print(num_palindromic(286))
#print(num_palindromic(196196871))