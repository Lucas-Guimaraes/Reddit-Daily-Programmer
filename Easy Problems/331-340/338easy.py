#https://www.reddit.com/r/dailyprogrammer/comments/79npf9/20171030_challenge_338_easy_what_day_was_it_again/

import calendar

def simple(year, month, day):
    #uses calendar to grab the idx number - list for idx number
    givenday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return givenday[calendar.weekday(year, month, day)]

# Introduction
print("Welcome to calendar")
print("Insert a year, month, and day")
print("\n~*~--------~*~\n")

#input
cal = True
while cal:
    #setup
    y = raw_input('Year: ')
    m = raw_input('Month: ')
    d = raw_input('Day: ')

    if d == 'q' or m == 'q' or y == 'q':
        break
    if y.isdigit() and m.isdigit() and d.isdigit():
        y, m, d = int(y), int(m), int(d)
        if 8000 > y and 13 > m and 32 > d:
            print(simple(y, m, d))

raw_input("Press enter to exit.")