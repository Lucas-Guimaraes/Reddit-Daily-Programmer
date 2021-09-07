#https://www.reddit.com/r/dailyprogrammer/comments/3bi5na/20150629_challenge_221_easy_word_snake/
#I'm sure this could be refactored

def word_snake(lst):

	matrix = []
	cur_dir = 0
	cur_space = 0
	cur_bottom = 0
	space_trigger = False
	for i in range(len(lst)):
		#Going down
		if cur_dir == 1:
			#Logic basically says "If first, just append it. If not, check if item already exists
			#It gets a little more complicated for appending a new item when going down
			for x in range(cur_bottom+1, len(lst[i][1:]) + cur_bottom+1):
				if i == 1:
					matrix.append((cur_space * ' ') + lst[i][x])
				else:
					if len(matrix) > x:
						matrix[x] += (cur_space * ' ') + lst[i][x - cur_bottom]
					else:
						matrix.append(((cur_space + len(matrix[len(matrix) - 1]) - 2) * ' ') + lst[i][x - cur_bottom])
			cur_dir += 1
			cur_bottom += len(lst[i][1:])

		#Going up
		elif cur_dir == 3:
			#If current space is fine, don't worry about it. If not, reformat for space
			for x in range(1, len(lst[i][1:])+1):
				if len(max(matrix, key=len)) == len(matrix[-x - 1]):
					matrix[-x - 1] += ((cur_space * ' ') + lst[i][x])
				else:
					cur_space = (len(max(matrix, key=len)) - len(matrix[-x - 1])) - 1
					matrix[-x - 1] += ((cur_space * ' ') + lst[i][x])
			cur_dir = 0
			cur_bottom = len(matrix) - len(lst[i])

		#Going right
		else:
			#If first, append, else, add. The right item will never be appended after the first time
			if i == 0:
				matrix.append(lst[i])
				cur_space = len(lst[i]) - 1
			else:
				matrix[cur_bottom] += lst[i][1:]
				cur_space = len(lst[i]) - 2
			cur_dir += 1


	#Prints matrix
	for m in matrix:
		print(m)

#Test Case
word_snake(["HOLA","ANDINA", "ARROZ", "ZOPA", "APPLE", "ELMO", "ORANGE", "END", "DOG", "GONE", "ESCALATORS", "SEASON", "NEW", "WIN", "NEANDERTHAL"])
