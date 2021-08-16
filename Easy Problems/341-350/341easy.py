#https://www.reddit.com/r/dailyprogrammer/comments/7eh6k8/20171121_challenge_341_easy_repeating_numbers/

import collections

def repeat_num(n):
    repeat_dict = {}
    #Loopers outer then inner to get the beginning and end
    for i in range(len(n)):
        for x in range(i, len(n)):
            #Grabs segment to check - and throws out invalid ones
            check = n[i:x]
            if len(check) <= 1:
                continue

            #Checks the count of n. If above 1, add it to dict
            check_count = n.count(check)
            if check_count > 1:
                repeat_dict[int(check)] = check_count

    #Orders by keys
    ol = collections.OrderedDict(sorted(repeat_dict.items()))

    #Print code
    if repeat_dict == {}:
        print(0)
    for k, v in ol.items():
        print(str(k) + ":" + str(v))

#Intro
print("Welcome to Repeating Numbers")
print("Give a big number; find out all smaller chunks of occurrences of it repeating")
print("\n~*~----------------~*~\n")

#Run code
repeat = True
while repeat:
    n = raw_input()
    if n.lower() == 'q':
        break
    if n.isdigit():
        repeat_num(n)

print("Press enter to exit")

#Test case
#repeat_num('11325992321982432123259')


