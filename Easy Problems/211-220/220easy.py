# https://www.reddit.com/r/dailyprogrammer/comments/504rdh/20160829_challenge_281_easy_something_about_bases/

#Extra space included to stop at 17
hex_16 = "0123456789abcdef "
def check_base(c_str):
    base = hex_16.find(max(str(c_str))) + 1
    while 17 > base:

        print('base {} => {}'.format(base, int(c_str, base)))
        new_str = hex_16[base]
        base = hex_16.find(max(str(new_str))) + 1

#Introduction text
print("Welcome to Check Base!")
print("Put in a number from base 2 to base 16")
print("The output? All possible bases that number could be.")
print("...and its lowest number in Base 10")
print("\n~*~--------~*~\n")

base = True
while base:
    i = raw_input()
    if i.lower() == 'q':
        break
    hex = True
    for x in i:
        if x not in hex_16:
            hex = False
            break
    if hex:
        i = i.replace(" ", "")
        check_base(i)

raw_input("Press enter to exit.")
#test case
#check_base(("21"))