#https://www.reddit.com/r/dailyprogrammer/comments/pwons/2192012_challenge_11_easy/
#https://medium.com/@sunil01966/tomohiko-sakamotos-algorithm-finding-the-day-of-the-week-e168d34d8402
#the Sakamoto Algorithm

user_day = int(raw_input("Give me a day!"))
user_month = int(raw_input("Give me a month!"))
user_year = int(raw_input("Give me a year!"))
result = 0

def day_check(x):
    if x == 1:
        print "mon"
    elif x == 2:
        print "tues"
    elif x == 3:
        print "wed"
    elif x == 4:
        print "thurs"
    elif x == 5:
        print "fri"
    elif x == 6:
        print "sat"
    elif x== 7:
        print "sun"

def what_day(day_input, month_input, year_input):
    table_array = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    print table_array
    if (month_input < 3):
        year_input = year_input - 1
    result = (year_input + year_input / 4 - year_input / 100 + year_input / 400 + table_array[month_input - 1] + day_input) % 7
    day_check(result) 
    
what_day(user_day, user_month, user_year)

raw_input()