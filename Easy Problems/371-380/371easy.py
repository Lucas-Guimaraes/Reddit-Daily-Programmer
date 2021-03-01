# https://www.reddit.com/r/dailyprogrammer/comments/ab9mn7/20181231_challenge_371_easy_n_queens_validator/
def qcheck(spaces):
    possible_spaces = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
                       'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
                       'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                       'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
    row_lst = ['1', '2', '3', '4', '5', '6', '7', '8']
    col_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # north west to south eaaast
    diagonal_sw_ne = {'a1': ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'],
                      'a2': ['a2', 'b3', 'c4', 'd5', 'e6', 'f7', 'g8'],
                      'a3': ['a3', 'b4', 'c5', 'd6', 'e7', 'f8'],
                      'a4': ['a4', 'b5', 'c6', 'd7', 'e8'],
                      'a5': ['a5', 'b6', 'c7', 'd8'],
                      'a6': ['a6', 'b7', 'c8'],
                      'a7': ['a7', 'b8'],
                      'a8': ['a8'],
                      'b1': ['b1', 'c2', 'd3', 'e4', 'f5', 'g6', 'h7'],
                      'c1': ['c1', 'd2', 'e3', 'f4', 'g5', 'h6'],
                      'd1': ['d1', 'e2', 'f3', 'g4', 'h5'],
                      'e1': ['e1', 'f2', 'g3', 'h4'],
                      'f1': ['f1', 'g2', 'h3'],
                      'g1': ['g1', 'h2'],
                      'h1': ['h1']}
    # south east to north west
    diagonal_se_nw = {'h1': ['h1', 'g2', 'f3', 'e4', 'd5', 'c6', 'b7', 'a8'],
                      'h2': ['h2', 'g3', 'f4', 'e5', 'd6', 'c7', 'b8'],
                      'h3': ['h3', 'g4', 'f5', 'e6', 'd7', 'c8'],
                      'h4': ['h4', 'g5', 'f6', 'e7', 'd8'],
                      'h5': ['h5', 'g6', 'f7', 'e8'],
                      'h6': ['h6', 'g7', 'f8'],
                      'h7': ['h7', 'g8'],
                      'h8': ['h8'],
                      'g1': ['g1', 'f2', 'e3', 'd4', 'c5', 'b6', 'a7'],
                      'f1': ['f1', 'e2', 'd3', 'c4', 'b5', 'a6'],
                      'e1': ['e1', 'd2', 'c3', 'b4', 'a5'],
                      'd1': ['d1', 'c2', 'b3', 'a4'],
                      'c1': ['c1', 'b2', 'a3'],
                      'b1': ['b1', 'a2'],
                      'a1': ['a1']}
    queens = []
    seen_spaces = []
    # tracks the current column we're on
    for i in range(len(spaces)):

        c_space = col_lst[i] + str(spaces[i])
        queens.append(c_space)
        # this tracks columns
        for c in range(len(spaces)):
            n_space = col_lst[c] + str(spaces[i])
            if n_space == c_space:
                continue
            seen_spaces.append(n_space)
        # this tracks rows
        for r in range(len(spaces)):
            n_space = col_lst[i] + row_lst[r]
            if n_space == c_space:
                continue
            seen_spaces.append(n_space)

        # southwest to northeast
        for value in diagonal_sw_ne.values():
            if c_space in value:
                for v in value:
                    if v == c_space:
                        continue
                    seen_spaces.append(v)

        # southeast to northwest
        for value in diagonal_se_nw.values():
            if c_space in value:
                for v in value:
                    if v == c_space:
                        continue
                    seen_spaces.append(v)

    for i in queens:
        if i in seen_spaces:
            return False

    return True


def qfix(spaces):
    first_check = qcheck(spaces)
    if first_check == True:
        return "{} is a valid n_queens solution. No swaps necessary".format(spaces)
    spaces = tuple(spaces)
    for i in range(0, len(spaces)):
        for a in range(0, len(spaces)):

            new_spaces = list(spaces)
            new_spaces[i], new_spaces[a] = new_spaces[a], new_spaces[i]
            new_check = qcheck(new_spaces)
            if new_check == True:
                return "{} is a valid n_queens solution. Swap number {} and {} from your original input".format(new_spaces, str(i + 1),
                                                                                       str(a + 1))
    return "No valid swap for {}".format(spaces)


print("\n~*~----------------~*~\n")

print("Welcome to n queens validator!")
print("A queen in chess can move in any octigonal direction")
print("So north, west, east, south, and diagonally")
print("The goal of the n queens validator is to attempt to find a valid n queens solution!")
print("\n~*~----------------~*~\n")
print("You will input your numbers like this: ")
print("1 2 3 4 5 6 7 8")
print("Each of them will determine what row the number is on, while the column is each index")
print("So since the first number is 1, it is on the first column, titled A")
print("Don't worry if you get it wrong!")
print("We'll show you if you can get a valid n queens solution by swapping two numbers.")
print("\n~*~----------------~*~\n")
print("Example of a valid n queens solution using only four numbers:")
print()
print("2, 4, 1, 3")
print("* 4 * *")
print("* * * 3")
print("2 * * *")
print("* * 1 *")
print()
print("None of the numbers are touching each other diagonally")
print("\n~*~----------------~*~\n")
n_queens_check = True
while n_queens_check:
    board_put = raw_input("Please put in your board. 'q' to quit: ")

    if board_put == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. Non case sensitive.").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
        n_queens_check = False
        continue
    board_lst = board_put.split()

    if len(board_lst) > 8:
        print("{} is more numbers than this program can handle!".format(board_lst))
        continue
    
    invalid_digit == False
    for s in board_lst:
        if s.isdigit() is False:
            print("{0} in {1} is not a valid digit!".format(s, board_lst))
            invalid_digit == True
            break

    if invalid_digit == False:
        board_lst = [int(s) for s in board_lst]

    print(qfix(board_lst))

raw_input("Press Enter to exit.")

# print(qcheck([2, 4, 1, 3]))
# print(qcheck([4, 2, 7, 3, 6, 8, 5, 1]))
# print(qcheck([2, 5, 7, 4, 1, 8, 6, 3]))
# print(qcheck([5, 3, 1, 4, 2, 8, 6, 3]))
# print(qcheck([5, 8, 2, 4, 7, 1, 3, 6]))
# print(qcheck([4, 3, 1, 8, 1, 3, 5, 2]))
# print(qfix([8, 6, 4, 2, 7, 1, 3, 5]))
# print(qfix([8, 5, 1, 3, 6, 2, 7, 4]))
# print(qfix([4, 6, 8, 3, 1, 2, 5, 7]))
# print(qfix([7, 1, 3, 6, 8, 5, 2, 4]))