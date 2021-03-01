# https://www.reddit.com/r/dailyprogrammer/comments/22fgs1/472014_challenge_157_easy_the_winning_move_xgames/
# combinations = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 5, 7], [3, 6, 9], [4, 5, 6], [7, 8, 9]]
def tic_tac_solver(player, string):

    #start code, including winning combos
    string = string.replace('\n', '')
    mod_str = string
    opponent = ''
    blank = '-'
    winner = ''
    combinations = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7], [2, 4, 6], [2, 5, 8], [3, 4, 5], [6, 7, 8]]

    if player == 'X':
        opponent = 'O'
    else:
        opponent = 'X'


    for i in range(len(string)):
        #checks if valid spot
        if string[i] == blank:
            #checks which valid spots the combination can fit in
            for combo in combinations:
                if i in combo:
                    test_str = ''
                    #this gives the string that tests the combination with our player
                    for c in combo:
                        if i == c:
                            test_str += player
                        else:
                            test_str += string[c]
                    if blank in test_str:
                        test_str = ''

                    #if the set of the test string only has all of the player object, it makes the winning string
                    if len(set(test_str)) == 1:
                        for x in range(len(string)):
                            if x in combo:
                                winner += player
                            else:
                                winner += string[x]
                    mod_str = string

    #If a winning move, it will return the winning move. If not, string.
    if len(winner) == 0:
        return "There are no winning moves!"

    winner = winner[0:3] + "\n" + winner[3:6] + "\n" + winner[6:9]
    return winner


#Introduces the player
print("Welcome to tic tac toe solver!")
print("This program takes two inputs:")
print("Which player you are, and a game board")
print("From there, it will suggest a move")
print("Which player you are can be done either as 'X' or '0'")
print("For the board, please use '-' to indicate blank tiles")
print("Example input:")
print("x")
print("xx-")
print("-xo")
print("oo-")
print("\n~*~----------------~*~\n")
faulty_input = True
valid_inputs = ['X', 'O']

#Player input; checks player input
while faulty_input:
    player_input = raw_input("Give me an input: ")
    player_input = player_input.replace(' ', '').replace('0', '0')
    player_input = player_input.upper()
    if len(player_input) == 1 and player_input in valid_inputs:
        faulty_input = False
    else:
        print("{} is not a valid input!".format(player_input))

faulty_input = True
valid_inputs.append('-')
faulty_line = False
while faulty_input:
    board = ''
    for i in range(3):
        line = raw_input("Give me a line: ")
        line = line.replace(' ', '').replace('x', 'X').replace('o', 'O').replace('0', 'O')
        for chr in line:
            if chr not in valid_inputs:
                print("that's not a valid line!")
                faulty_line = True
        board += line + "\n"

    board = board[0:11]
    if len(board) == 11 and faulty_line is False:
        faulty_input = False
print("\n~*~----------------~*~\n")
print(tic_tac_solver(player_input, board))
raw_input("\nPress Enter to exit.")

#print(tic_tac_solver("X", """XX-
#-XO
#OO-"""))

#print(tic_tac_solver('x', """--O
#OXX
#---"""))

#print(tic_tac_solver("O", """O-X
#-OX
#---"""))