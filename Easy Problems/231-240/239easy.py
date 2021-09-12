# https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

def three_game(n):
    lst = []
    while n > 1:
        if n / 3 == 0 or n % 3 != 0:
            if (n + 1) % 3 == 0:
                n = n + 1
                lst.append((n, '+1'))
                continue
            elif (n - 1) % 3 == 0:
                n = n - 1
                lst.append((n, '-1'))
                continue
        elif n / 3 == 1:
            lst.append(1)
            break
        else:
            n = n / 3
            lst.append((n, '0'))
    for i in lst:
        if type(i) == tuple:
            str_i = [str(x) for x in i]
            str_i = " ".join(str_i)
        else:
            str_i = str(i)
        print(str_i)


print("Welcome to Play Three Game")
print("Insert a number, and we will show a fast way to get it all the way down to one")
print("...By only dividing by three, adding by one, and adding by two")
print("\n~*~----------------~*~\n")

play_three_game = True
while play_three_game:
    number = raw_input()
    if number.lower() == 'q':
        break
    if number.isdigit():
        three_game(int(number))

raw_input("Press enter to exit.")
# three_game(1000)