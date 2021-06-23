# https://www.reddit.com/r/dailyprogrammer/comments/1qdw40/111113_challenge_141_easy_monty_hall_simulation/

import random


def monty_hall_trials(trials):
    switch = 0
    stay = 0

    for x in range(trials):

        prize_door = random.randrange(0, 3)
        picked_door = random.randrange(0, 3)

        # these add points for Stay and Switch tactics
        if picked_door == prize_door:
            stay = stay + 1

        if picked_door != prize_door:
            switch = switch + 1

    stay_percentage = 100 * stay / trials
    switch_percentage = 100 * switch / trials

    tactics = """Tactic 1 (Staying): {0}
Tactic 2 (Switching): {1}""".format(stay_percentage, switch_percentage)
    return tactics


print("Welcome to monty hall!")
print("This program will print out your chances of staying as tactic 1, and switching as tactic 2.")
print("\n~*~----------------~*~\n")
montyhall = True
while montyhall:
    num = raw_input("How many times would you like to run the simulation? ('q' to exit): ")
    if num.isdigit():
        print(monty_hall_trials(int(num)))
    if num == 'Q' or num == 'q':
        montyhall = False
        break

raw_input("Press enter to exit")
# print(monty_hall_trials(1000))
