#https://www.reddit.com/r/dailyprogrammer/comments/4jom3a/20160516_challenge_267_easy_all_the_places_your/

def dog_didnt_win(win):
    lst = []
    ordinal = {'1': 'st', '2': 'nd', '3': 'rd'}
    exceptions = [11, 12, 13]
    for i in range(1, 101):
        if i == win:
            continue
        elif str(i)[-1] in ordinal.keys() and i not in exceptions:
            lst.append(str(i) + ordinal[str(i)[-1]])
        else:
            lst.append(str(i) + 'th')
    return lst

#Explination
print("Welcome to Dog Didn't Win")
print("Your dog entered a competition. Put in the place they won")
print("...And you'll get all the places they *didn't* win!")
print("\n~*~----------------~*~\n")

#Checks input, quit case included
dog_gone = True
while dog_gone:
    place = raw_input()
    if place.islower() == 'q':
        break
    if place.isdigit():
        print(dog_didnt_win(int(place)))

#Test case
#print(dog_didnt_win(1))