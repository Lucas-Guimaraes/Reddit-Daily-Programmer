#https://www.reddit.com/r/dailyprogrammer/comments/q4c34/2242012_challenge_15_easy/
#easy15justifytxt

justify_read = open("easy15justify.txt","r")
justify = (justify_read.read())

while True:
    justify_text = raw_input("'l' for left, 'r' for right justifying text: ")
    
    if justify_text == 'l':
        print justify.ljust(40, '-')
        break
    elif justify_text == 'r':
        print justify.rjust(40, '-')
        break
    else:
        "That's not a proper input!"
        
raw_input()