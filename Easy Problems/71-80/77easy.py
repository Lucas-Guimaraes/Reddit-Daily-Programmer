#https://www.reddit.com/r/dailyprogrammer/comments/wn3ld/7162012_challenge_77_easy_enumerating_morse_code/

cache = {}
#Recursion is fun - this works on going through recursion
def morse(n):
    if n<0:
        return []
    if n==0:
        return ['']
    if n in cache:
        return cache[n]
    cache[n]=[i+'.' for i in morse(n-1)]+[i+'-' for i in morse(n-2)]
    return cache[n]

def quit_check(i):
    if i == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive: ").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            return True
    return False

print("Input a number. Any number longer than 36 will crash the program")
print("Any number past 30 will be slow, so go at your own peril.")
print("From it, we will print out all combinations of morse where '.' == 1, and '-' == 2")

print("\nExample Input:")
print("5")

print("\nExample Output:")
print(".....  ...-  ..-.  .-..  -...  .--  -.-  --.")

print("\n~*~----------------~*~\n")

morsey = True
while morsey:
    m_put = raw_input("Input your morse number (or Q) here: ").lower().replace(' ', '')
    if quit_check(m_put):
        break
    if m_put.isdigit():
        m_put = int(m_put)
        if m_put > 36:
            print("{} is too big! Remember: Below 36!".format(m_put))
        else:
            print(morse(m_put))
    else:
        print("{} is not a digit!".format(m_put))
    
raw_input("Press enter to exit")
#print(morse(35))