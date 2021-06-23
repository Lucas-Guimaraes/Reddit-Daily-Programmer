# https://www.reddit.com/r/dailyprogrammer/comments/106go0/9202012_challenge_100_easy_sleep_cycle_estimator/


import math

sleep_cycle = 90
am_pm_checker = ['am', 'pm']


def sleep_cycles(minutes):
    digit_list = [minutes - sleep_cycle * i for i in range(3, 7)]

    digit_list_copy = digit_list

    # this converts each of them to numbers
    index = -1
    for sleep_time in digit_list_copy:
        index += 1

        if sleep_time < 0:
            digit_list.remove(sleep_time)
            sleep_time = 1440 + sleep_time
            digit_list.insert(index, sleep_time)


    sleep_cycle_list = []

    # this converts each of the numbers to AM/PM

    for sleep_time in digit_list:

        convert_hour = int(math.floor(sleep_time / 60))
        convert_minute = sleep_time % 60
        am_or_pm = ''
        if convert_minute == 0:
            convert_minute = '00'
        if convert_hour > 12:
            am_or_pm = 'PM'
            convert_hour -= 12
        else:
            am_or_pm = 'AM'
            if convert_hour < 1:
                convert_hour = 12

        converted_string = "{0}:{1} {2}".format(convert_hour, convert_minute, am_or_pm)
        sleep_cycle_list.append(converted_string)

    return sleep_cycle_list


def time_to_num(hours, minutes, am_pm):
    if am_pm == 'pm':
        hours += 12

    minutes = hours * 60 + minutes

    return sleep_cycles(minutes)


def invalid(inv_str):
    inv_str = " ".join(inv_str)
    return "\n{0} is an invalid input\n".format(inv_str)


print("\n*--------*--------*\n")
print("Hello! Welcome to Sleep Cycle\n")
raw_input("Press Enter to Continue")
print("\n*--------*--------*\n")
print("This application takes one input: Your ideal bed time.")
print("The output?\n")
print("The time you need to go to bed to get a proper amount of sleep cycles in")
print("That would be 3-6 sleep cycles")
print("A sleep cycle is compromised of 90 minutes.")
print("So you would need at least 270 minutes of sleep - that's 4 and a half hours.")
print("6 sleep cycles, the maximum, would be 540. 9 hours.")
raw_input("\nPress Enter to Continue")
print("\n*--------*--------*\n")
sleep_test = True
wakeup_time = ''

while sleep_test:
    no_loop = False

    instructions = raw_input("Do you need the instructions? If so, type 'y' for yes and press enter.\n If not, just press enter. \n")
    if instructions == 'y':
        print("Print out the format like this: 'hour minute timezone'")
        print("ONLY these three")
        print("Examples of valid input:")
        print("1 00 pm")
        print("2 00 am")
        print("11          59         pm")
        print("4 20   am")
        print("Examples of invalid input:")
        print("4 12 peeeem")
        print("6:49 am")
        print("13:49")
        print("42 4 aM")
        print("Hopefully this helps.\n")
    wakeup_time = raw_input("Give me your sleep time. An example of a valid format: 1 00 pm (for '1:00 PM') \n"
                            "Input sleep time here: ")
    wakeup_time = wakeup_time.split()


    if len(wakeup_time) != 3:
        no_loop = True
    else:
        if wakeup_time[0].isdigit() is False:
            no_loop = True
        elif int(wakeup_time[0]) < 0 or int(wakeup_time[0]) > 12:
            no_loop = True


        if wakeup_time[1].isdigit() is False:
            no_loop = True
        elif int(wakeup_time[1]) < 0 or int(wakeup_time[1]) > 59:
            no_loop = True

        if wakeup_time[2] not in am_pm_checker:
            print(wakeup_time[2])
            print(am_pm_checker)
            no_loop = True

    if no_loop is True:
        print(invalid(wakeup_time))
        continue
    else:
        sleep_test = False

    index_1 = wakeup_time.pop(1)
    index_0 = wakeup_time.pop(0)
    wakeup_time.insert(0, int(index_0))
    wakeup_time.insert(1, int(index_1))



final_sleep_times = time_to_num(wakeup_time[0], wakeup_time[1], wakeup_time[2])
if wakeup_time[1] == 0:
    wakeup_time[1] = '00'

print(wakeup_time)
final_wake_time = "{0}:{1} {2}".format(wakeup_time[0], wakeup_time[1], wakeup_time[2].upper())

print("\n*--------*--------*\n")
print("Your chosen time is {}".format(final_wake_time))
print("The ideal bedtimes would be {0}, {1}, {2}, and {3}".format(final_sleep_times[3], final_sleep_times[2],
                                                                  final_sleep_times[1], final_sleep_times[0]))
print("\n*--------*--------*\n")
raw_input("Press Enter to Exit")

