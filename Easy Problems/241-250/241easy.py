#https://www.reddit.com/r/dailyprogrammer/comments/3t0xdw/20151116_challenge_241_easy_unicode_chess/

#generates the chess board we use
def gen_chessboard():
	row_lst = [8, 7, 6, 5, 4, 3, 2, 1]
	col_lst = '   abcdefgh'
	board = []
	for i in range(len(row_lst)):
		if i % 2 == 0:
			s = ' ' + str(row_lst[i]) + "|" + '.*.*.*.*'
		else:
			s = ' ' + str(row_lst[i]) + "|" + '*.*.*.*.'
		board.append(list(s))
	board.append(list('  +--------'))
	board.append(list(col_lst))
	return board

#Fen input
def fen_input(s):
	g = gen_chessboard()
	inputs = s.split('/')

	#makes the new rows
	new_rows = []
	for x in range(0, 8):
		while len(inputs[x]) < 8:
			new_put = ''
			for i in inputs[x]:
				if i.isdigit():
					new_put += (int(i) * ' ')
				else:
					new_put += i
			inputs[x] = new_put
		new_rows.append(inputs[x])
		for col in range(0, 8):
			if new_rows[x][col] != ' ' and new_rows[x][col].isdigit() == False:
				g[x][col + 3] = new_rows[x][col]


	for row in g:
		print(''.join(row))

print("Hello! Welcome to Ascii Chess!")
print("The inputs available are seven /'s, with 1-8 characters.")
print("\n~*~----------------~*~\n")

check = True

# this tests our input
while check:
	chess_put = raw_input("Please put in a usable action: ")
	if chess_put.lower() == 'Q':
		break
	if chess_put.count('/') == 7:
		print()
		fen_input(chess_put)
		print()


raw_input("Press enter to exit.")

#test case
#fen_input('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
#fen_input('snbqkbns/pppppppp/8/8/4P3/8/PPPP1PPP/SNBQKBNS')