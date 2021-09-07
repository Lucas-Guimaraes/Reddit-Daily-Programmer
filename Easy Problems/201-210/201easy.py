#https://www.reddit.com/r/dailyprogrammer/comments/2vc5xq/20150209_challenge_201_easy_counting_the_days/

import datetime

def time_away(d):
    #If the date changes while using this application
    now = datetime.date.today()
    #Tries to get the date
    try:
        future = datetime.date(d[0], d[1], d[2])
        return "{} days from {} to {}".format((future-now).days, now, future)
    #If getting the date fails, it tells us that the date we put is invalid
    except:
        return "{}-{}-{} is an invalid date. Please try again.".format(d[0], d[1], d[2])

#Input
print("Welcome to Counting Days.")
print("This program will tell you how many days left from the current date")
print("Example Input:")
print("2021 09 08")
print("Year, Month, Date")
print("\n~*~----------------~*~\n")

#Run Code

counting = True

while counting:
    d = raw_input()
    #Quit code
    if d.lower() == "q":
        break
    d = d.split()
    #Tries to split in 3
    if len(d) == 3:
        #Checks if all 3 are digits
        if d[0].isdigit() and d[1].isdigit() and d[2].isdigit():
            #Makes our list items into integers
            d = [int(i) for i in d]
            print(time_away(d))

raw_input("Press enter to exit.")

#print(time_away([2021, 9, 8]))