# https://www.reddit.com/r/dailyprogrammer/comments/13hmz3/11202012_challenge_113_easy_stringtype_checking/
def str_type(check_str):
    #this tries to see if it is a float/decimal
    if '.' in check_str:
        try:
            float(check_str)
            return "float"
        except:
            pass
    #testing for integer
    else:
        try:
            int(check_str)
            return "int"
        except:
            pass
    #tests if it's a valid date, since numbers didn't work
    if len(check_str.split('-')) == 3:
        return "date"
    else:
        return "text"
        
#handles all input and explains the program to the user.
print("Welcome to string checker!")
print("This program takes one input, a string")
print("Followed by it's output, telling you what type it is")
print("The four types are Integer, Float, Date, and Text")
print("\n~*~----------------~*~\n")
str_test = raw_input("Give me a string to check!: ")
print("\n~*~----------------~*~\n")
print(str_type(str_test))
print("\n~*~----------------~*~\n")
raw_input("Press enter to exit")

#print(str_type('+123'))
#print(str_type('123.456'))
#print(str_type('20-11-2012'))
#print(str_type('hello'))
