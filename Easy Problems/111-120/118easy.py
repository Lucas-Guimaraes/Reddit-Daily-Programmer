#https://www.reddit.com/r/dailyprogrammer/comments/16z9oj/012113_challenge_118_easy_date_localization/
#all this does is check the timer, so no input
from datetime import datetime

def datetime_format(string):
    now = datetime.now()

    string = string.replace("%l", now.strftime("%f"))
    string = string.replace("%s", now.strftime("%S"))
    string = string.replace("%m", now.strftime("%M"))
    string = string.replace("%h", now.strftime("%I"))
    string = string.replace("%H", now.strftime("%H"))
    string = string.replace("%c", now.strftime("%p"))
    string = string.replace("%d", now.strftime("%d"))
    string = string.replace("%m", now.strftime("%m"))
    string = string.replace("%y", now.strftime("%Y"))
    return string
print(datetime_format("The minute is %m! The hour is %h."))
raw_input("\nPress enter to exit.")

# "%l": Milliseconds (000 to 999)
# "%s": Seconds (00 to 59)
# "%m": Minutes (00 to 59)
# "%h": Hours (in 1 to 12 format)
 # "%H": Hours (in 0 to 23 format)
 # "%c": AM / PM (regardless of hour-format)
 # "%d": Day (1 up to 31)
 # "%M": Month (1 to 12)
 # "%y": Year (four-digit format)