# https://www.reddit.com/r/dailyprogrammer/comments/urqcx/682012_challenge_62_easy/

# num_lst gets the sub lowest
# after the sub lowest, it sees if that number is less than sum_n
# if yes, then true
# if no, then false

def ullman_puzzle(num_lst, sum_n, sub):
    lowest_sum = 0
    for i in range(sub):
        low_num = min(num_lst)
        lowest_sum += low_num
        num_lst.remove(low_num)
    if sum_n > lowest_sum:
        return True
    else:
        return False


def quit_check(i):
    if i == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive: ").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            return True
    return False


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


print("Hello! Welcome to the Ullman Puzzle")
print("You will give three inputs: The first is a list of floats")
print("The second is how many of these numbers to add")
print("The third number will be the number to compare the sum to")

print("\n Example Input:")
print("4.4 3 2 1 5")
print("3")
print("7")

print("\n Example Output:")
print("True")

print("\n Explination:")
print("1 + 2 + 3, the lowest 3 numbers from the '3' earlier, all equal 6")
print("6 is lower than 7")

print("\n~*~----------------~*~\n")

ullman_puz = True
quitting = False
while ullman_puz:
    if quitting == True:
        ullman_puz = False
        break

    # input our list of floats
    input_1 = True
    while input_1:
        flt_lst = raw_input("Input your list of floats. q to exit (works at any input screen): ").replace(',', '')
        q_check = quit_check(flt_lst)

        if q_check == True:
            quitting = True
            input_1 = False
            break
        flt_lst = flt_lst.split()

        for i in flt_lst:
            if not isfloat(i):
                print("{0} from {1} isn't valid number!".format(i, flt_lst))
                continue

        flt_lst = [float(i) for i in flt_lst]
        input_1 = False

    input_2 = True
    while input_2:
        check_num = raw_input("How many numbers to check?: ").replace(' ', '')
        q_check = quit_check(check_num)

        if q_check == True:
            input_2 = False
            quitting = True
            break

        if check_num.isdigit():
            input_2 = False
            check_num = int(check_num)
            continue
            
        else:
            print("{0} is not a number!".format(check_num))
            continue

    # This obtains our comparison number
    input_3 = True
    while input_3:
        comp_num = raw_input("What number will the smallest sum of {} numbers from the list be compared to?: ".format(
            str(check_num))).replace(' ', '')
        q_check = quit_check(comp_num)

        if q_check == True:
            input_3 = False
            quitting = True
            break

        if isfloat(comp_num):
            input_3 = False
            comp_num = float(comp_num)
            continue

        else:
            print("{0} is not a float nor a number!".format(comp_num))
            continue

    # input 1, input 3, input 2 into the ullman puzzle
    print(ullman_puzzle(flt_lst, comp_num, check_num))

# isfloat
# quit_check

raw_input("Press Enter to exit.")

# print(ullman_puzzle([18.1, 55.1, 91.2, 74.6, 73.0, 85.9, 73.9, 81.4, 87.1, 49.3, 88.8, 5.7, 26.3, 7.1, 58.2, 31.7, 5.8, 76.9, 16.5, 8.1, 48.3, 6.8, 92.4, 83.0, 19.6], 98.2, 3)) #returns true
# print(ullman_puzzle([18.1, 55.1, 91.2, 74.6, 73.0, 85.9, 73.9, 81.4, 87.1, 49.3, 88.8, 5.7, 26.3, 7.1, 58.2, 31.7, 5.8, 76.9, 16.5, 8.1, 48.3, 6.8, 92.4, 83.0, 19.6], 18, 3)) #returns false

