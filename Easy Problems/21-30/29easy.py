#https://www.reddit.com/r/dailyprogrammer/comments/r8a70/3222012_challenge_29_easy/

#Paldrine_lst is to make the initial list
#the formatted string prints it all out as one string
#the non formatted string removes non alphanumeric characters
#then makes it lowercase
#uses the poem of 'dammit i'm mad' by Demetri Martin

palindrome_lst = [line.rstrip('\n') for line in open("easy29supplement.txt")] 

palindrome_formatted_str = "\n".join(palindrome_lst)

palindrome_str = "".join(palindrome_lst)
palindrome_str = "".join(filter(str.isalnum, palindrome_str))
palindrome_str = palindrome_str.lower()

def palindrome_check(pal_str):
    if pal_str == pal_str[::-1]:
        return "%s is a palindrome!" % palindrome_formatted_str
    else:
        return "%s is not a palindrome!" % palindrome_formatted_str

print palindrome_check(palindrome_str)
raw_input()