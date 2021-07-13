# https://www.reddit.com/r/dailyprogrammer/comments/2dvc81/8182014_challenge_176_easy_spreadsheet_developer/

alpha_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
              'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
              'X': 24, 'Y': 25, 'Z': 26}


def spreadsheet(str_put):
	str_put = str_put.replace('&', ':')
	str_put = str_put.split(':')
	spreadsheet_lst = []

	for i in range(0, len(str_put), 2):
		a, b = str_put[i], str_put[i+1]

		ax, ay, bx, by = alpha_dict[a[0]], int(a[1:]), alpha_dict[b[0]], int(b[1:])


		if ay > by:
			num_rep = ay-by
		elif ay < by:
			num_rep = by-ay
		else:
			num_rep = 1

		saving_spreadsheet = True
		while saving_spreadsheet:
			spreadsheet_lst.append('{0}, {1}'.format(str(ax), str(ay)))
			if ax > bx:
				ax -= 1
			elif ax < bx:
				ax += 1
			else:
				ax = alpha_dict[a[0]]
				if ay > by:
					ay -= 1
				elif ay < by:
					ay += 1
				elif ay == by:
					saving_spreadsheet = False
					break
#		for x in range(num_rep):

	print(len(spreadsheet_lst))
	for s in spreadsheet_lst:
		print(s)

print("Welcome to excel spreadsheet!")
print("Example input:")
print("A1:B3")
print("Example output:")
print("""6\n
1, 1\n
2, 1\n
1, 2\n
2, 2\n
1, 3\n
2, 3""")

print("\n~*~----------------~*~\n")

check_sheet = True

while check_sheet:
    cells = raw_input().upper()
    if cells == 'Q':
        break
    spreadsheet(cells)

raw_input("Press enter to exit")

#test cases below
#spreadsheet('A1:B3')
#spreadsheet('A1:B3:D5:Q14')