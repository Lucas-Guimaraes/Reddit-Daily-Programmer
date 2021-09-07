# https://www.reddit.com/r/dailyprogrammer/comments/2ygsxs/20150309_challenge_205_easy_friendly_date_ranges/

month = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
         '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}


def friendly_date(dates):
    dates = dates.split()
    first_date, second_date = dates[0], dates[1]
    y_1, m_1, d_1 = first_date.split('-')
    y_2, m_2, d_2 = second_date.split('-')
    first, second = ['', '', ''], ['', '', '']

    # Find Years:
    year_check = int(y_2) - int(y_1)
    month_check = int(m_2) - int(m_1)
    day_check = int(d_2) - int(d_1)
    if y_1 == y_2:
        if m_1 != m_2 or (m_1 == m_2 and d_1 == d_2):
            second[2] = y_2
    elif year_check >= 2 or (year_check == 1 and month_check >= 0):
        first[2], second[2] = y_1, y_2

    # Find Months:
    if year_check == 0 and month_check == 0:
        first[0] = month[m_1]
    else:
        first[0], second[0] = month[m_1], month[m_2]

    # Days
    if year_check == 0 and month_check == 0 and day_check == 0:
        first[1] = str(int(d_1)) + get_suffix(d_1)
    else:
        first[1], second[1] = str(int(d_1)) + get_suffix(d_1), str(int(d_2)) + get_suffix(d_2)

    # Handles if dates same,
    if first_date == second_date:
        date_string = first[0] + " " + first[1] + ", " + second[2]

    # Month, day, year for each string
    else:
        date_string = ''
        if first[0] != '':
            date_string += first[0] + " "
        if first[1] != '':
            date_string += first[1]
        if first[2] != '':
            date_string += ", " + first[2]
        if len(first[0] + first[1] + second[2]) != 0:
            date_string += " - "
        if second[0] != '':
            date_string += second[0] + " "
        if second[1] != '':
            date_string += second[1]
        if second[2] != '':
            date_string += ", " + second[2]

    return date_string


def get_suffix(day):
    day = int(day)
    if (day / 10) % 10 == 1:
        return "th"
    elif day % 10 == 1:
        return "st"
    elif day % 10 == 2:
        return "nd"
    elif day % 10 == 3:
        return "rd"
    else:  # everything else
        return "th"


# Intro
print("Welcome to Friendly Date Ranges")
print("Example Input:")
print("2015-12-01 2016-02-03")
print("\n~*~--------~*~\n")

# Input
friendly = True
while friendly:
    d = raw_input()
    if d.islower() == 'q':
        break

    date = d.split()
    one, two = date[0], date[1]
    if '-' in one and '-' in two:
        y1, m1, d1 = one.split('-')
        y2, m2, d2 = two.split('-')
        if y1.isdigit() and m1.isdigit() and d1.isdigit() and y2.isdigit() and m2.isdigit() and d2.isdigit():
            print(friendly_date(d))

raw_input("Press enter to exit.")

# test cases

# print(friendly_date('2015-07-01 2015-07-04'))
# print(friendly_date('2015-12-01 2016-02-03'))
# print(friendly_date('2015-12-01 2017-02-03'))
# print(friendly_date('2016-03-01 2016-05-05'))
# print(friendly_date('2017-01-01 2017-01-01'))
# print(friendly_date('2022-09-05 2023-09-04'))