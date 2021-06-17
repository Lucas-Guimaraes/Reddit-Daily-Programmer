#https://www.reddit.com/r/dailyprogrammer/comments/12qi5b/1162012_challenge_111_easy_star_delete/

def star_delete(string):
    star_removed = ''
    removal_list = []
    star_final = ''
    
    #for every number in the string, check if an * exists
    for i in range(len(string)):
        if string[i] == '*':
            star = i
            before_star = i - 1
            after_star = i + 1
            #this scenario makes sure the * is removed, if only that can be removed
            if i == len(string) and i-1 == -1:
                removal_list.append(star)
            #removes the one before the star
            elif i == len(string):
                removal_list.append(star)
                removal_list.append(before_star)
            #removes star and after star
            elif i-1 == -1:
                removal_list.append(star)
                removal_list.append(after_star)
            #if all other scenarios are eliminated, this removes the one before, during, and after the star
            else:
                removal_list.append(star)
                removal_list.append(before_star)
                removal_list.append(after_star)
        #continue with the loop
        else:
            continue
    #if the integer is not in the removal list, it will be added to star removed      
    for i in range(len(string)):
        if i in removal_list:
            pass
        else:
            star_removed += string[i]


    return star_removed

print("Welcome to Star Delete!")
print("This program will remove any characters with a '*'")
print("Along with the character preceding, and the character following.")
print("\nExample input:")
print("adf*lp")
print("\nExample output:")
print("adp")
print("\n~*~----------------~*~\n")
star_string = raw_input("Give me a string to use!:\n\n")
print("\n~*~----------------~*~\n")
print(star_delete(star_string))
print("\n~*~----------------~*~\n")
print("Press enter to exit.")

#print(star_delete("adf*lp"))
#print(star_delete("a*o"))
#print(star_delete("*dech*"))
#print(star_delete("de**po"))
#print(star_delete("sa*n*ti"))
#print(star_delete("abc"))

raw_input()