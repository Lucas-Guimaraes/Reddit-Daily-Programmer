#https://www.reddit.com/r/dailyprogrammer/comments/53ijnb/20160919_challenge_284_easy_wandering_fingers/

#'284easy.txt' is a supplementary file to this program.


file = open('284easy.txt', 'r')
word_lst = []

#Grabs the word list
for line in file.readlines():
    new = line.replace("\n", "")
    word_lst.append(new)

#Loops through word list
def wandering_fingers(word, lst):
	final_lst = []
	for i in lst:
		if check_word(word, i) != None:
			final_lst.append(check_word(word, i))
	return final_lst

#Checks every word ran through
def check_word(word, target):
	last_idx = 0
	cur_idx = 1

	#Initial tests - first and last letter, target len
	if word[0] != target[0] or word[-1] != target[-1] or len(target) < 5:
		return None

	#Checks every letter
	for i in target[1:]:
		if last_idx > cur_idx:
			return None

		if i in word[cur_idx:]:
			last_idx = cur_idx
			add = len(word[:last_idx])
			cur_idx = word[last_idx:].index(i) + add

		else:
			return None

	return target


print(check_word('goalie', 'galilee'))

#Introductory text
print("Welcome to Messy Keys")
print("Input a string")
print("This program will output all possible words to make by only removing words")
print("\n~*~----------------~*~\n")

#Looping
messykeys = True

while messykeys:
	m = raw_input()

	#Quit and type check
	if m.lower == "q":
		break
	if m.isalpha():
		print(wandering_fingers(m, word_lst))

raw_input("\nPress enter to exit.")