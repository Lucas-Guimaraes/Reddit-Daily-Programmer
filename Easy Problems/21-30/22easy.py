#https://www.reddit.com/r/dailyprogrammer/comments/qr0hg/3102012_challenge_22_easy/

def joint_list(first_list, second_list):
    for item in second_list:
        if item not in first_list:
            first_list.append(item)
    return first_list
print joint_list(["hey", "hi", "yeah"], ["yeah", "test", "yeah"])
raw_input()