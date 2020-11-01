# https://www.reddit.com/r/dailyprogrammer/comments/pzo4w/2212012_challenge_13_easy/

def is_leap_year(leap_check):
    # modulo 4, followed by 100, followed by 400
    if (leap_check % 4) == 0 and (leap_check % 100) != 0:
        return True
    elif (leap_check % 400) == 0:
        return True
    else:
        return False


# checks if number is greater than zero
def gt_zero(number_use):
    if number_use > 0:
        return True
    else:
        return False


# counts our day
def count_day(x_month, y_day):
    year_index = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    x_month = int(x_month)
    y_day = int(y_day)
    for i in range(x_month - 1):
        total += int(year_index[i])
    total += y_day
    return total


def valid_submission():
    # this makes sure the submission is valid
    while True:
        month_input = int(raw_input("Give me a digit between 1-12 for the month!: "))
        day_input = int(raw_input("Give me a digit for a day!: "))
        year_input = int(raw_input("Give me four digits for a year!: "))
        leap_year = is_leap_year(int(year_input))
        # this calculates whether the month is valid
        if month_input < 13 and gt_zero(month_input) is True:
            # April, June, September, December
            if month_input == 4 or month_input == 6 or month_input == 9 or month_input == 12:
                # check if the day is in the region
                if day_input < 31 and gt_zero(day_input) is True:
                    break
            # feb check
            elif month_input == 2:
                # check if leap year
                if leap_year is True:
                    if day_input < 30 and gt_zero(day_input) is True:
                        break
                # if not leap year for feb
                else:
                    if day_input < 29 and gt_zero(day_input) is True:
                        break
            # jan, march, may, july, august, october, november
            else:
                if day_input < 32 and gt_zero(day_input) is True:
                    break

    result = count_day(month_input, day_input)
    if month_input > 2 and leap_year is True:
        result += 1
    return result

print valid_submission()

        