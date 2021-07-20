#https://www.reddit.com/r/dailyprogrammer/comments/6e08v6/20170529_challenge_317_easy_collatz_tag_system/

def collatz(str):
    #Dictionary to use
    dict = {'a':'bc','b':'a','c':'aaa'}
    while len(str) > 1:
        print(str)
        #Grabs anything after the first two items + end is the Collatz Dict
        str = str[2:] + dict[str[0]]
    #Prints last result
    print(str)
    return

#Introduction text
print("Welcome to Collatz Tag System")
print("Input a string with only 'a' in it")
print("\n~*~----------------~*~\n")

# Checks input, quit case included

tag_system = True
while tag_system:
    at_lst = raw_input("")
    at_lst = at_lst.lower()
    if at_lst == 'q':
        break
    if set(at_lst) == set(['a']):
        collatz(at_lst)

raw_input("Press enter to exit.")