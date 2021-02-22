# https://www.reddit.com/r/dailyprogrammer/comments/ruiob/452012_challenge_36_easy/
#this video explains it well: https://www.youtube.com/watch?v=LejoPGtliTs
def a_thousand_lockers():
    lockers = [False for i in range(1, 1001)]
    for student in range(1, 1001):
        #print(student)
        for locker in range(0, 1000, student):
            if lockers[locker] is False:
                lockers[locker] = True
            else:
                lockers[locker] = False

    locker_count = 0
    lockers_open = []
    for locker in range(len(lockers)):
        if lockers[locker] is True:
            locker_count += 1
            lockers_open.append(locker)

    return locker_count, lockers_open

lock_count, opened_doors = a_thousand_lockers()
print("The amount of lockers opened is {0}\nThe lockers left open are:\n{1}".format(lock_count, opened_doors))
raw_input("Print enter to exit.")