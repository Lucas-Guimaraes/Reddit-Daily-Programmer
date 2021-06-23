# https://www.reddit.com/r/dailyprogrammer/comments/1k7s7p/081313_challenge_135_easy_arithmetic_equations/
import random
import operator

#This game handles math problems
def math_game():
    do_not_exit = True
    #If the user chooses to not put an exit input, the game will keep going.
    #The input is just lowercase 'exit'
    while do_not_exit:
    
        #This dictionary works to detect a map of operators. 
        op_map = {"+": operator.add,
                  "-": operator.sub,
                  "*": operator.mul}
        operators = ['*', '+', '-']
        
        #Randomizes the problem
        op_lst = [random.choice(operators) for i in range(3)]

        num_lst = [random.randrange(0, 10) for i in range(4)]

        # '0 x 0 + 0 - 0' (but all randomized)
        question_lst = [str(num_lst[0]), op_lst[0], str(num_lst[1]), op_lst[1], str(num_lst[2]), op_lst[2], str(
            num_lst[3])]
        question = " ".join(question_lst)
        answer = eval(question)
        print(question)
        user_input = raw_input(">")

        #Tells if the user input works
        if user_input == 'exit':
            raw_input("Goodbye!")
            do_not_exit = False
        try:
            int(user_input)

            if int(user_input) == answer:

                print('Correct!')
            else:
                print('Incorrect. Answer was {}'.format(answer))
        except:
            print("That's not a valid answer!")

    return

#Starts the game
math_game()