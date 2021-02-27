#https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/

def same_necklace(initial, reform):
    if initial == "" and reform == "":
        return True

    for i in range(len(reform)):
        if initial == (reform[i:] + reform[:i]):
            print(i)
            return True
    return False

print("Welcome to same necklace!")
print("This device takes two strings: The initial letters of the necklace, and reformed")
print("So for example, the necklace spells nicole")
print("These variations are all possible:")
print("icolen")
print("coleni")
print("olenic")
print("lenico")
print("enicol")
print("nicole")
print("The last letter of the string can be moved to the front, and the front letter can be moved to the last")
print("Take 'nicole' again - 'icolen' and 'enicol' are both possible")
print("Because it's the first or last letter being used")
print("So for icolen or enicol, the program will print True")
print("However, if the variation is not possible - i.e, neiloc, it will return false")
print("\n~*~----------------~*~\n")
first_str = raw_input("Please give me your initial necklace:\n")
second_str = raw_input("\nAnd the variation to check:\n")
print("\n~*~----------------~*~\n")

print(same_necklace(first_str, second_str))
raw_input("\nPress Enter to exit.")

#print(same_necklace("nicole", "icolen"))
#print(same_necklace("nicole", "lenico"))
#print(same_necklace("nicole", "coneli"))
#print(same_necklace("aabaaaaabaab", "aabaabaabaaa"))
#same_necklace("abc", "cba") => false
#same_necklace("xxyyy", "xxxyy") => false
#same_necklace("xyxxz", "xxyxz") => false
#same_necklace("x", "x") => true
#same_necklace("x", "xx") => false
#same_necklace("x", "") => false
#same_necklace("", "") => true