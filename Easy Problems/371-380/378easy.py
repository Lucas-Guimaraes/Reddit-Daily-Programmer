# https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/

# starts the havel hakimi algorithm
def hh(suspects):
    # sorts all of the suspects in

    new_sus = suspects
    while True:
        new_sus.sort(reverse=True)
        # deletes all 0's, and then goes through the list
        for i in reversed(range((len(new_sus)))):
            if new_sus[i] == 0:

                del new_sus[i]
            else:
                break

        # if the list is empty, the program ends and nobody lied
        if len(new_sus) == 0:
            return True

        # if the len of the list is greater than the highest number, then it returns false
        n = new_sus.pop(0)
        if len(new_sus) < n:
            return False

        # since n was removed from the pool, all indexes need to be brought down by one
        for i in range(n):
            new_sus[i] = new_sus[i] - 1


print("Welcome to the Havel Hikami algorithm!")
print("You will give one input: A list of numbers")
print("Explaining this algorithm may take a while to get")
print("We start out with our list. 3, 1, 3, 2, 1, 0")

print("\nStep #1:\n")

print("First, we order our list by biggest number.")
print("3, 3, 2, 1, 1, 0")

print("\nStep #2:\n")

print("Cull all 0's")
print("3, 3, 2, 1, 1")

print("\nStep #3:\n")

print("Check if the list is empty")
print("3, 3, 2, 1, 1 - still has 5 items in the list")
print("If the list ever does become empty, we exit the program.")
print("Remember Step #3 as 'Checkpoint #1'. We'll come back to this.")

print("\nStep #4:\n")

print("We remove the biggest number and store it to its own spot.")
print("'3', [3, 2, 1, 1]")

print("\nStep #5:\n")

print("Compare our biggest number to the amount of items in the rest of the list")
print("Is 3 greater than 4?")
print("No.")
print("If the biggest number ever becomes larger than the rest of the items in ithe list, we exit the program.")
print("Remember Step #5 as 'Checkpoint #2'. We'll come back to this.")

print("\nStep #6:\n")

print("Starting from the beginning of the list, we minus the biggest numbers by 1")
print("We only do this until the biggest number has been exhausted")
print("The current list is 3, 2, 1, 1")
print("We minus the first 3 items by one")
print("So the list becomes 2, 1, 0, 1")

print("\nStep #7:\n")

print("Repeat steps #1-7 until the program reaches a conclusion.")
print("If we were to repeat this until a conclusion:")
print("Step #1 (Loop 2): 2 1 1 0")
print("Step #2 (Loop 2): 2 1 1 ")
print("Step #3 (Loop 2): List is not empty, continue.")
print("Step #4 (Loop 2): [2], [1, 1]")
print("Step #5 (Loop 2): 2 is equal to length 2, so we continue")
print("Step #6 (Loop 2): 1, 1. We minus both by 1 to make 0, 0")
print("Step #1 (Loop 3): 0 0 can not be ordered.")
print("Step #2 (Loop 3): Cull all 0's. The list is now empty.")
print("Step #3 (Loop 3): Since the list is empty, we return it as true.")
print("\nThe two conclusions are (Hope you remembered the checkpoints!):\n")
print("#1 - Step #3 - The list is empty. No suspects are lying. Returns True, as outlined in the example.")
print("#2 - Step #5 - A suspect is lying because they've met more than the amount of people left. Returns False")


print("\n~*~----------------~*~\n")

hh_check = True
while hh_check:
    sus_lst = raw_input("Please put in your list. 'q' to quit: ").replace(',', '')

    if sus_lst == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. Non case sensitive.").lower()
        if sus_lst == 'yes' or answer == 'y':
            print("Goodbye.")
        hh_check = False
        continue

    sus_lst = sus_lst.split()
    invalid_digit = False
    for s in sus_lst:
        if s.isdigit() is False:
            print("{0} in {1} is not a valid digit!".format(s, sus_lst))
            invalid_digit = True
            break
    if invalid_digit == False:
        sus_lst = [int(s) for s in sus_lst]

    print(hh(sus_lst))

raw_input("Press Enter to exit.")

# test inputs
# print(hh([]))
# print(hh([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]))
# print(hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]))
# print(hh([3, 1, 2, 3, 1, 0]))
# print(hh([4, 2, 0, 1, 5, 0]))
#print(hh([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]))