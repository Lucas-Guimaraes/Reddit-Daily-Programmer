# https://www.reddit.com/r/dailyprogrammer/comments/yqydh/8242012_challenge_91_easy_sleep_sort/
# this was an interesting time.
# concurrent.futures is for multiprocessing
# https://www.youtube.com/watch?v=IEEhzQoKtQU

import time
import threading


def sleepy(num):
    time.sleep(num)
    print(str(num) + ' ')


def sleep_sort(lst):
    for i in lst:
        start_this = threading.Thread(target=sleepy, args=[int(i)])
        start_this.start()

def conclusion(timer):
    time.sleep(timer)
    print("")
    print("*--------*--------*")
    print("")
    raw_input("Press Enter to exit.")
    quit()

def end_program(timer):
    end_this = threading.Thread(target=conclusion, args=[timer])
    end_this.start()


print("*--------*--------*")
print("")
print("Hello! Welcome to Sleep Sort")
print("")
raw_input("Press Enter to Continue")
print("")

print("*--------*--------*")
print("")
print("This application takes one Input - a list")
print("Your list of numbers should be typed out like this: 'number number number'")
print("An example:")
print("4 2 4 3")
print("From it, we will print them out in order - each of them will print based on their seconds.")
print("So 4 will take 4 seconds, and 3 will take 3 seconds.")
print("Since this is a sort, 3 will print before 4")
print("But 4 will only take one second longer than 3")
print("")
raw_input("Press Enter to Continue")
print("")

print("*--------*--------*")
print("")

integer_list = []
while len(integer_list) == 0:
    initial_list = (raw_input("Please give me your list to continue: "))

    initial_list = initial_list.split()
    index_tracker = len(initial_list)

    for i in range(0, index_tracker):
        current_check = initial_list[i]
        if current_check.isdigit():
            integer_list.append(initial_list[i])
        else:
            pass

print("You entered this as your list:\n {}".format(integer_list))
print("")
print("Now printing your sort!")
print("")
sleep_sort(integer_list)
end_timer = int(max(integer_list))+1
end_program(end_timer)
