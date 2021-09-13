#https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/

#Hours
hours = {'00': 'twelve', '01': 'one', '02': 'two', '03': 'three', '04': 'four', '05': 'five', '06': 'six', '07': 'seven', '08': 'eight', '09': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'one', '14': 'two', '15': 'three', '16': 'four', '17': 'five', '18': 'six', '19': 'seven', '20': 'eight', '21': 'nine', '22': 'ten', '23': 'eleven'}

#Every minute
minute_dict = {
    "0": "",    "1": "one",    "2": "two",    "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"
}

#Every ten minutes
minute_tens_dict = {
    "2": "twenty",    "3": "thirty",    "4": "forty",    "5": "fifty"
}

#Function used
def talking_clock(h, m):
    #Gets hour
    hour = hours[h]

    #Checks if AM or PM
    if int(h) >= 12:
        ampm = "pm"
    else:
        ampm = "am"

    minute = ''

    #Checks if 20 or larger
    if int(m) >= 20:
        minute_bigger, minute_smaller = minute_tens_dict[m[0]], minute_dict[m[1]]
        if len(minute_smaller) > 0:
            minute = " " + minute_bigger + " " + minute_smaller
        else:
            minute = " " + minute_bigger

    #10-19
    elif int(m) >= 10:
        minute = " " + minute_dict[m]

    #1-9
    elif int(m) >= 1:
        minute = " oh " + minute_dict[m[1]]

    talking = "It's " + hour + minute + " " + ampm
    return talking


# Intro text
print("Welcome to Talking Clock")
print("Input a time")
print("Example Input: 02:21")
print("The Hour number goes from 0 to 23 - the Minute number goes from 0 to 59")
print("\n~*~----------------~*~\n")

tick_tock = True
while tick_tock:
    time = raw_input()
    if time.lower() == 'q':
        break
    if ':' in time:
        time = time.split(':')
        hour, minute = time[0], time[1]
        if hour.isdigit() and minute.isdigit():
            if 23 >= int(hour) >= 0 and 59 >= int(minute) >= 0:
                print(talking_clock(hour, minute))


#Test Cases

#print(talking_clock('00', '00'))
#print(talking_clock('01', '30'))
#print(talking_clock('12', '05'))
#print(talking_clock('14', '01'))
#print(talking_clock('20', '29'))
#print(talking_clock('21', '00'))