# https://www.reddit.com/r/dailyprogrammer/comments/3wshp7/20151214_challenge_245_easy_date_dilemma/

# year month date
def date_dilemma(date):
    #Checks which seperator
    if '-' in date:
        date = date.split('-')
    elif '/' in date:
        date = date.split('/')
    elif ' ' in date:
        date = date.split(' ')

    day, month, year = date[0], date[1], date[2]
    #Switch around
    if len(year) == 2 and len(day) == 4:
        day, year = year, day
    if month > 31:
        day, month = month, day

    #Checks if not enough digits
    if len(day) != 2:
        day = "0" + day
    if len(month) != 2:
        month = "0" + month
    if len(year) != 4:
        year = "20" + year

    #Combines and returns date
    date = year + "-" + month + "-" + day
    return date

#Introduction
print("Welcome to Date Dilemma!")
print("Put in a date. This checker will fix it")
print("\n~*~--------~*~\n")

#While loop
dilemma = True
while dilemma:
    w = raw_input()
    if w.lower() == 'q':
        break
    print(date_dilemma(w))

raw_input("Press enter to exit.")

#test case
#print(date_dilemma("2/13/15"))