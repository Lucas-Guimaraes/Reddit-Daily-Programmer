#https://www.reddit.com/r/dailyprogrammer/comments/36cyxf/20150518_challenge_215_easy_sad_cycles/

#Sad Cycle itself
def sad_cycle(base, n):
	lst = []
	while n > 1:
        #Convert to string, have total
		str_n = str(n)
		total = 0
        
        #Add to total
		for i in str_n:
			total += int(i) ** base
		
        #If n is in list, cycle finish. Else, append
        n = total
		if str(n) in lst:
			break
		lst.append(str(total))
	
    return ', '.join(lst)

# Input
print("Welcome to Sad Cycle!")
print("Insert a number and get its sad cycle!")

print("\n~*~----------------~*~\n")

# Run code
sad = True
while sad:
	base_put = raw_input("Give me a base: ")
	int_put = raw_input("Give me an integer: ")
	if base_put.islower() == 'q' or int_put.islower() == 'q':
		break
	if base_put.isdigit() and int_put.isdigit():
		print(sad_cycle(int(base_put), int(int_put)))

print("Press enter to exit")

#Test Case
#print(sad_cycle(2, 12))