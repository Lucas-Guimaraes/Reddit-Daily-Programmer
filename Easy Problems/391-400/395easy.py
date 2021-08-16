#https://www.reddit.com/r/dailyprogrammer/comments/o4uyzl/20210621_challenge_395_easy_nonogram_row/

#Nonogram Row Function
def nonogram(lst):
    final = []
    cur = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            cur += 1
        if lst[i] == 0 or (lst[i] == 1 and len(lst)-1 == i):
            final.append(cur)
            cur = 0

    return final

#Checks if nonogram
def is_nono(nonogram):
    for i in nonogram:
        if i not in '01':
            return False
    return True

# Intro
print("Welcome to nonogram!")
print("Put in a list of 1's and 0's")
print("\n~*~----------------~*~\n")

counting = True

#Input
while counting:
    row = raw_input("Put in your string: ").lower()
    if row == 'q':
        break
    row = row.split()
    if is_nono(row):
        row = [int(x) for x in row]
        print(nonogram(row))

#Exit
raw_input("Press enter to exit.")