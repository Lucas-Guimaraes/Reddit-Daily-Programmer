#https://www.reddit.com/r/dailyprogrammer/comments/60ibay/20170320_challenge_307_easy_base_255_part1/

#Base 255

def base255(lst):
	final_str = ''
	#loops list
	for l in range(len(lst)):
		word = lst[l]
		for w in range(len(word)):
			final_str += word[w]
			if word[w] == '+':
				final_str += '+'
			if w == len(word)-1 and l != len(lst)-1:
				final_str += '+,'


	return final_str

print(base255(['abc+def', 'ghjh', 'klmno++p+']))