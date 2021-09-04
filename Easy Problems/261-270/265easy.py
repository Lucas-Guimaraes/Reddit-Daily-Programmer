#https://www.reddit.com/r/dailyprogrammer/comments/4htg9t/20160504_challenge_265_easy_permutations_and/

import itertools

#Grabs permutations
def perm(x, n):
    lst = [i for i in range(n)]
    lst = list(itertools.permutations(lst))
    result = lst[x-1]
    return result

#Grabs combinations
def comb(x, n, t):
    lst = [i for i in range(n)]
    lst = list(itertools.combinations(lst, t))
    result = lst[x-1]
    return result

#Extracts numbers from words
def int_lst(s):
    numbers = []
    for word in s.split():
        word = word.replace("th","").replace("st","").replace("nd","").replace("rd","")
        if word.isdigit():
            numbers.append(int(word))
    return numbers

#Intro
print("Welcome to permutations and combinations")
print("Example inputs:")
print("what is the 240th permutation of 6")
print("24th combination of 3 out of 8")
print("\n~*~--------~*~\n")

#Input
calculate = True
while calculate:
    t = raw_input()
    t = t.lower()
    if t == 'q':
        break
    lst = int_lst(t)
    if 'permutation' in t:
        place, amt = lst[0], lst[1]
        print(perm(place, amt))
    if 'combination' in t:
        place, rge, amt = lst[0], lst[1], lst[2]
        print(comb(place, amt, rge))
raw_input("Press enter to exit.")

#Test Cases
#print(comb(3, 6, 3))
#print(perm(240, 6))