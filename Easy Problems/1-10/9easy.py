#https://www.reddit.com/r/dailyprogrammer/comments/pu1rf/2172012_challenge_9_easy/

test_var = []
concact = 0
def OrderedList(x):
    test_var = list(x)
    test_var = sorted(test_var)
    test_var = ''.join(map(str, test_var))
    return test_var
    
while True:
    check_input = raw_input("Put 'int' for Letter and 'num' for Number: ")
    if check_input == 'int':
        concact = str(raw_input("Put in a string!: "))
        print OrderedList(concact)
        break
    elif check_input == 'num':
        concact = int(raw_input("Put in a number!: "))
        print OrderedList(concact)
        break
    else:
        "Print a letter or a number!"
        
raw_input()