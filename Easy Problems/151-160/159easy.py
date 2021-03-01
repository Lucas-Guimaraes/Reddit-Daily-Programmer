# https://www.reddit.com/r/dailyprogrammer/comments/23lfrf/4212014_challenge_159_easy_rock_paper_scissors/
# rock paper scissors lizard spock
import random


def rpsls():
    play = True
    options = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    print("Hello! Welcome to Rock Paper Scissors...")
    print("...Lizard Spock.")
    print("This works similar to the classic rps")
    print("Rock smashes paper")
    print("Paper covers rock")
    print("Scissors cuts paper.")
    print("Except with two added characters: Lizard, and Spock")
    print("Rock beats Scissors and Lizard")
    print("Paper beats Rock and Spock")
    print("Scissors beats Lizard and Paper")
    print("Lizard beats Paper and Spock")
    print("Spock beats Scissors and Rock")
    print("You will put in one input: your choice of five. And compete against the computer's choice.")
    print("\n~*~----------------~*~\n")
    while play:
        player_choice = raw_input("Please input your choice. 'q' will quit the program: ")
        computer_choice = random.choice(options)
        player_choice = player_choice.replace(' ', '').lower()
        if player_choice == 'q':
            play = False
        if player_choice not in options:
            print(" is not a valid choice!")
            continue
        if player_choice == 'rock':
            if computer_choice == 'scissors' or computer_choice == 'lizard':
                print("Computer chose {}. You win!").format(computer_choice)
            elif computer_choice == 'paper' or computer_choice == 'spock':
                print("Computer chose {}. You lose!").format(computer_choice)
            else:
                print("Both you and the computer chose {}. It's a tie!").format(computer_choice)

        elif player_choice == 'paper':
            if computer_choice == 'rock' or computer_choice == 'spock':
                print("Computer chose {}. You win!").format(computer_choice)
            elif computer_choice == 'lizard' or computer_choice == 'scissors':
                print("Computer chose {}. You lose!").format(computer_choice)
            else:
                print("Both you and the computer chose {}. It's a tie!").format(computer_choice)

        elif player_choice == 'scissors':
            if computer_choice == 'lizard' or computer_choice == 'paper':
                print("Computer chose {}. You win!").format(computer_choice)
            elif computer_choice == 'rock' or computer_choice == 'spock':
                print("Computer chose {}. You lose!").format(computer_choice)
            else:
                print("Both you and the computer chose {}. It's a tie!").format(computer_choice)

        elif player_choice == 'lizard':
            if computer_choice == 'paper' or computer_choice == 'spock':
                print("Computer chose {}. You win!").format(computer_choice)
            elif computer_choice == 'scissors' or computer_choice == 'rock':
                print("Computer chose {}. You lose!").format(computer_choice)
            else:
                print("Both you and the computer chose {}. It's a tie!").format(computer_choice)

        elif player_choice == 'spock':
            if computer_choice == 'scissors' or computer_choice == 'rock':
                print("Computer chose {}. You win!").format(computer_choice)
            elif computer_choice == 'paper' or computer_choice == 'lizard':
                print("Computer chose {}. You lose!").format(computer_choice)
            else:
                print("Both you and the computer chose {}. It's a tie!").format(computer_choice)
        print("")


rpsls()
raw_input("\nPress Enter to exit.")

# rock kills scissors and lizard
# paper kills rock and spock
# scissors kills lizard and paper
# lizard kills paper and spock
# spock kills scissors and rock
# [1, 2, 3, 4, 5]
# [1 kills 3, 4]
# [2 kills 5, 1]
# [3 kills 4, 2]
# [4 kills 2, 5]
# [5 kills 1, 3]