# https://www.reddit.com/r/dailyprogrammer/comments/t78m8/542012_challenge_48_easy/

def evens_and_odds(lst):
    evens = []
    odds = []
    for i in lst:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    
    result = evens + odds
    return result

print("Welcome to List Organizer!")
print("This program takes a list of integers and puts even numbers before odds")
print("\n~*~--------~*~\n")
str_put = raw_input("Please give me your list:\n")
i_lst = str_put.split()
i_lst = [int(x) for x in i_lst]
print("")
print(evens_and_odds(i_lst))

raw_input("Press enter to exit")
#evens_and_odds([43, 23, 54, 6, 7, 10, 23, 42, 12, 4, 6, 8, 02, 94, 59])