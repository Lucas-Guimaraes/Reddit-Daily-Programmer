# https://www.reddit.com/r/dailyprogrammer/comments/r0r3h/3172012_challenge_27_easy/
# checks the century
def century(year):
    date_suffix = ["th", "st", "nd", "rd"]
    year = str(year)
    xtra = True
    if int(year) % 100 == 0:
        xtra = False
    if int(year) >= 1000:
        cent = year[0:2]
    elif int(year) >= 100:
        cent = year[0]
    else:
        cent = 1
        xtra = False

    cent = int(cent)

    if xtra:
        print cent
        cent = cent+1

    if cent % 10 in [1, 2, 3] and cent not in [11, 12, 13]:
        suffix = date_suffix[cent % 10]
    else:
        suffix = date_suffix[0]
    return "%s%s century" % (cent, suffix)


# checks if leap year
def leap(year):
    if year % 4 != 0:
        return "common year"
    elif year % 100 != 0:
        return "leap year"
    elif year % 400 != 0:
        return "common year"
    else:
        return "leap year"


def combo_string(year):
    final_century = century(year)
    final_leap = leap(year)
    return "The year %s is a %s in the %s" % (year, final_leap, final_century)


year_input = int(raw_input("YO! Give me a year and I'll tell you what century it's in, and if it's a leap year: "))

print combo_string(year_input)

raw_input()