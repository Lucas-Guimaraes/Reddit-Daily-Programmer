# https://www.reddit.com/r/dailyprogrammer/comments/tb2h0/572012_challenge_49_easy/

import random

def monty_hall():
    winner = random.randint(1, 3)
    choices = [1, 2, 3]
    result_lst = ['car' if i == winner else 'goat' for i in range(1, 4)]
    goat_doors = [i for i in range(1, 4) if result_lst[i-1] == 'goat']
    invalid_answer = True

    while invalid_answer:
        first_answer = int(raw_input("""Pick a door! \n\n1\n2\n3\n\nYour answer here: """))
        if first_answer not in choices:
            print("{} is invalid. Please pick a valid answer!".format(first_answer))
            continue
        else:
            print("You've chosen door number {}!".format(first_answer))
            invalid_answer = False

    random_goat = random.randint(0, 1)
    if random_goat == 0:
        if goat_doors[0] == first_answer:
            reveal_goat_door = goat_doors[1]
        else:
            reveal_goat_door = goat_doors[0]
    else:
        if goat_doors[1] == first_answer:
            reveal_goat_door = goat_doors[0]
        else:
            reveal_goat_door = goat_doors[1]

    check_door = [reveal_goat_door, first_answer]
    remaining_door = set(choices) - set(check_door)
    remaining_door = list(remaining_door)
    remaining_door = remaining_door[0]


    print("You have revealed that there is a goat behind door number {}".format(reveal_goat_door))
    print("Would you like to Switch to Door {0} or stick to Door {1}?").format(remaining_door, first_answer)
    print("Type 'stay' to Stay, and 'switch' to Switch")
    invalid_answer_2 = True
    correct_answer = result_lst.index("car")+1
    while invalid_answer_2:
        second_answer = raw_input("Will you stay or will you go?: ")
        if second_answer == 'stay':
            invalid_answer_2 = False
        elif second_answer == 'switch':
            first_answer = remaining_door
            invalid_answer_2 = False
        else:
            "That's not a valid input!"

    if first_answer == correct_answer:
        print("\nYou've won a brand new car!")
    else:
        print("\nSorry. The correct answer was Door {}").format(correct_answer)
    # dothisalllater

def monty_hall_sim(n):
    doors = [1, 2, 3]

    stay = 0
    switch = 0
    for i in range(n):
        winner = random.choice(doors)
        player_choice = random.choice(doors)

        if player_choice == winner:
            stay += 1
        else:
            switch += 1
    f_n = float(n)
    stay_percent = stay / f_n * 100
    switch_percent = switch / f_n * 100
    return "After {0} runs, the amount of times it produced a win for staying is {1}% with {2} wins and a win for switching is {3}% with {4} wins".format(n, stay_percent, stay, switch_percent, switch)


monty_hall()
print("")
sim = int(raw_input("How many times would you like to try running the simulation? Try a real big number, like, something with at least 6 digits.\n"))
print(monty_hall_sim(sim))
raw_input("\nPress enter to exit")
