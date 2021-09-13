#https://www.reddit.com/r/dailyprogrammer/comments/5z4f3z/20170313_challenge_306_easy_pandigital_roman/

#int to roman
def int_to_Roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    #checks if num is divisible
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

#checks all tuples in loop
def pan_dig(loop):
    pan_digital = []
    exactly_once = []

    for i in loop:
        r = i[0]
        I_count, V_count, X_count, L_count, C_count, D_count, M_count = r.count("I"), r.count("V"), r.count("X"), r.count("L"), r.count("C"), r.count("D"), r.count("M")
        lst = [I_count, V_count, X_count, L_count, C_count, D_count, M_count]
        if lst == [1 for _ in range(7)]:
            exactly_once.append(i)
        if I_count > 0 and V_count > 0 and X_count > 0 and L_count > 0 and C_count > 0 and M_count > 0:
            pan_digital.append(i)
    return pan_digital, exactly_once



# Introduction
print("Roman Numerals")
print("Two inputs: The range of your start number, the range of your second")
print("And then we will find the amount of pan digital, and exactly once roman numerals")
print("\n~*~--------~*~\n")


#input
numerals = True
while numerals:
    start = raw_input("Start: ")
    end = raw_input("End: ")
    #quit
    if start.lower() == 'q' or end.lower() == 'q':
        break

    #if valid inputs
    if start.isdigit() and end.isdigit():
        start, end = int(start), int(end)
        loop_list = []
        
        #check range
        for i in range(start, end+1):
            r = int_to_Roman(i)
            loop_list.append((r, i))
        pan, e_o = pan_dig(loop_list)
        pan, e_o = ["{} ({})".format(x[0], x[1]) for x in pan], ["{} ({})".format(x[0], x[1]) for x in e_o]

        pan, e_o = ", ".join(pan), ", ".join(e_o)
        
        #print pan numbers, or 'no pan numbers'
        if len(pan) > 0:
            print(pan)
        else:
            print("There are no pan digital numbers between {} and {}!".format(start, end))

        #print each only once numbers
        if len(e_o) > 0:
            print(e_o)
        else:
            print("There are no pan digital numbers between {} and {}!".format(start, end))

raw_input("Press enter to exit.")