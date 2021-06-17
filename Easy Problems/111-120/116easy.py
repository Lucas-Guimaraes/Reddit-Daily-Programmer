# https://www.reddit.com/r/dailyprogrammer/comments/164zvs/010713_challenge_116_easy_permutation_of_a_string/

def permutate(str_ing):
    str_len = len(str_ing)
    
    #if there is only one character, just printing the string is enough
    if str_len == 1:
        print str_ing
        return

    #if there are two characters, we want to print both it and its variation
    elif str_len == 2:
        print str_ing
        print str_ing[1] + str_ing[0]
        return


    #this makes sure the count is given an initial number
    count = -1
    
    for i in range(str_len):
        count += 1
        permute_iterate = str_len - count
        #iterating letter
        il = str_ing[i]
        lst_start = list()
        lst_end = list()

        #calculates if at the end, followed by beginning
        if i == str_len:
            lst_start = str_ing[:i]

        elif i == 0:
            lst_end = str_ing[i+1:]

        else:
            lst_start = str_ing[:i]
            lst_end = str_ing[i+1:]

        #adds them as a list item
        lst_start = list(lst_start)
        lst_end = list(lst_end)
        full_lst = lst_start + lst_end
        
        #adds the permutated ones with each il
        #returns the list
        for x in range(permute_iterate):
            lst = full_lst[:x] + [il] + full_lst[x:]
            result = "".join(lst)
            print result
    return

print("Welcome to string permutations!")
print("This program takes one input and one output")
print("The input is a string")
print("The output is all permutations of that string!")

print("\n~*~----------------~*~\n")

perm_str = raw_input("Please put in your string to permutate!:\n")

print("\n~*~----------------~*~\n")

permutate(perm_str)

print("\n~*~----------------~*~\n")

raw_input("Press enter to exit.")

#test cases
#permutate("abbccc")