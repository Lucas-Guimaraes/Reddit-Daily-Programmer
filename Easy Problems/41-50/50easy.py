# https://www.reddit.com/r/dailyprogrammer/comments/teua8/592012_challenge_50_easy/

def credit_list(credit, lst):
    range_number = len(lst) - 1
    for item_one in (0, range_number):
        for item_two in range(1, range_number):
            if int(lst[item_one]) + int(lst[item_two]) == credit:
                return "The solution are in aisles: {} and {}. These items are {} and {}".format(str(item_one+1), str(item_two+1), lst[item_one], lst[item_two])
    return "We found no two items. Sorry."


print("*--------*--------*")
print("Hello! Welcome to Store Credit")
print("*--------*--------*")
input("Press Enter to Continue")
print("*--------*--------*")
print("This application takes two inputs - your amount of credits, and your list")
print("From it, we will see which two items to pick up")
print("If we can't find two items that add up to your credit number, we'll tell you.")
print("*--------*--------*")
input("Press Enter to Continue")
print("*--------*--------*")
user_credits = int(input("Please give me your amount of credits: "))
print("You entered {} for your credits amount".format(user_credits))
print("*--------*--------*")
item_string = input("Now for your list - please use spaces: ")
item_list = item_string.split()
print("You entered {} as your list".format(item_list))
print("*--------*--------*")
print(credit_list(user_credits, item_list))
print("*--------*--------*")
input("Press Enter to exit.")