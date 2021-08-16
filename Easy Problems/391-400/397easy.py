#https://www.reddit.com/r/dailyprogrammer/comments/oe9qnb/20210705_challenge_397_easy_roman_numeral/

def numcompare(a, b):
    roman_numerals = "MDCLXVI"

    for r in roman_numerals:
        #If in both
        if r in b and r in a:
            a_c, b_c = a.count(r), b.count(r)
            #If either is bigger, return
            if b_c > a_c:
                return True
            elif a_c > b_c:
                return False

        #If only in b
        elif r in b and r not in a:
            return True
        #If only in a
        elif r in a and r not in b:
            return False

    #Final False,, in-case no Truth is found
    return False

#Test Cases
print(numcompare("I", "I"))
print(numcompare("I", "II"))
print(numcompare("II", "I"))
print(numcompare("V", "IIII"))
print(numcompare("MDCLXV", "MDCLXVI"))
print(numcompare("MM", "MDCCCCLXXXXVIIII"))