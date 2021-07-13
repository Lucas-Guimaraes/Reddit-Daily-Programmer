# https://www.reddit.com/r/dailyprogrammer/comments/2cld8m/8042014_challenge_174_easy_thuemorse_sequences/

#function
def thru_morse(n):
    morse_lst = ['0', '01']
    count = n - 1
    #range for n
    for i in range(n+1):
        if i == 0 or i == 1:
            continue
        morse = morse_lst[i-1]

        new_morse = ''
        #makes the new morse
        for i in morse:
            if i == '0':
                new_morse += '1'
            elif i == '1':
                new_morse += '0'
        
        #adds the new morse
        morse = morse + new_morse
        morse_lst.append(morse)
    
    #fancy print
    print('nth' + (' ' * 7) + "Sequence")
    print('===========================================================================')
    space = ' ' * 9
    for i in range(len(morse_lst)):
        print(str(i) + space + morse_lst[i])

print("Welcome to morse sequence!")
print("Give a number for a sequence.")
print("For best results, try not to enter a number higher than twenty.")
print("\n~*~----------------~*~\n")

morse_seq = True

#Loop that keeps the program go until the user quits
while morse_seq:
    i = raw_input("How many sequences?: ")
    if i == 'q' or i == 'Q' :
        break
    if i.isdigit():
        thru_morse(int(i))

raw_input("\nPress enter to exit.")


#Test case
#thru_morse(30)