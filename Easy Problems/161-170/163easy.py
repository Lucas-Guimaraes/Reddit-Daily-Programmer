# https://www.reddit.com/r/dailyprogrammer/comments/25y2d0/5192014_challenge_163_easy_probability/

import random

def calc(i, a):
    i = float(i)
    a = float(a)
    i = round((i / a) * float(100), 2)
    fin_str = " " + str(i) + "%" + ((5 - len(str(i))) * " ")
    return fin_str

#print(round(float(m_dict['6'] / float(10000)), 2))
def dice_table():
    # t = ten, h = hundred, th = thousand, m = million
    # 10, 100, 1000, 10000, 100000, 1000000

    t_dict = {'1': 0, '2': 2, '3': 0, '4': 0, '5': 0, '6': 0}
    h_dict = {'1': 0, '2': 2, '3': 0, '4': 0, '5': 0, '6': 0}
    th_dict = {'1': 0, '2': 2, '3': 0, '4': 0, '5': 0, '6': 0}
    t_th_dict = {'1': 0, '2': 2, '3': 0, '4': 0, '5': 0, '6': 0}
    h_th_dict = {'1': 0, '2': 2, '3': 0, '4': 0, '5': 0, '6': 0}
    m_dict = {'1': 0, '2': 2, '3': 0, '4': 0, '5': 0, '6': 0}

    for i in range(10):
        roll = random.randint(1, 6)
        t_dict[str(roll)] += 1

    for i in range(100):
        roll = random.randint(1, 6)
        h_dict[str(roll)] += 1

    for i in range(1000):
        roll = random.randint(1, 6)
        th_dict[str(roll)] += 1

    for i in range(10000):
        roll = random.randint(1, 6)
        t_th_dict[str(roll)] += 1

    for i in range(100000):
        roll = random.randint(1, 6)
        h_th_dict[str(roll)] += 1

    for i in range(1000000):
        roll = random.randint(1, 6)
        m_dict[str(roll)] += 1

#    d_table = [t_dict, h_dict, th_dict, t_th_dict, h_th_dict, m_dict]

#    for d in d_table:
#        print(d)

    print("# of Rolls |" + "  1s     |" + "  2s     |" + "  3s     |" + "  4s     |" + "  5s     |" + "  6s     |")
    print("========================================================================")

    nums = [10, 100, 1000, 10000, 100000, 1000000]
    #ten dict
    print("10         | " + calc(t_dict['1'], nums[0]) + " | " + calc(t_dict['2'], nums[0]) + " | " + calc(t_dict['3'], nums[0]) + " | " + calc(t_dict['4'], nums[0]) + " | " + calc(t_dict['5'], nums[0]) + " | " + calc(t_dict['6'], nums[0]) + " |")

    #hundred dict
    print("100        | " + calc(h_dict['1'], nums[1]) + " | " + calc(h_dict['2'], nums[1]) + " | " + calc(h_dict['3'],
                                                                                                nums[1]) + " | " + calc(
        h_dict['4'], nums[1]) + " | " + calc(h_dict['5'], nums[1]) + " | " + calc(h_dict['6'], nums[1]) + " |")

    #thousand dict
    print("1000       | " + calc(th_dict['1'], nums[2]) + " | " + calc(th_dict['2'], nums[2]) + " | " + calc(th_dict['3'],
                                                                                                   nums[2]) + " | " + calc(
        th_dict['4'], nums[2]) + " | " + calc(th_dict['5'], nums[2]) + " | " + calc(th_dict['6'], nums[2]) + " |")

    #ten thousand dict
    print("10000      | " + calc(t_th_dict['1'], nums[3]) + " | " + calc(t_th_dict['2'], nums[3]) + " | " + calc(t_th_dict['3'],
                                                                                                       nums[3]) + " | " + calc(
        t_th_dict['4'], nums[3]) + " | " + calc(t_th_dict['5'], nums[3]) + " | " + calc(t_th_dict['6'], nums[3]) + " |")

    #hundred thousand dict
    print("100000     | " + calc(h_th_dict['1'], nums[4]) + " | " + calc(h_th_dict['2'], nums[4]) + " | " + calc(
        h_th_dict['3'],
        nums[4]) + " | " + calc(
        h_th_dict['4'], nums[4]) + " | " + calc(h_th_dict['5'], nums[4]) + " | " + calc(h_th_dict['6'], nums[4]) + " |")

    #million dict
    print("1000000    | " + calc(m_dict['1'], nums[5]) + " | " + calc(m_dict['2'], nums[5]) + " | " + calc(
        m_dict['3'],
        nums[5]) + " | " + calc(
        m_dict['4'], nums[5]) + " | " + calc(m_dict['5'], nums[5]) + " | " + calc(m_dict['6'], nums[5]) + " |")
    
print("Welcome to die table!")
print("This program takes no input!")
print("It just gives you a table that tells the probability for rolling a certain number on an amount of dice rolls")
print("So, what happens when you roll a six sided die 10 times? Maybe 100? How about 1000000?")
print("Find out!")
print("\n~*~----------------~*~\n")

dice_table()
raw_input("\nPress enter to exit.")