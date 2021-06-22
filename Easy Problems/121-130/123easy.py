# https://www.reddit.com/r/dailyprogrammer/comments/1cundw/042213_challenge_123_easy_sum_them_digits/

#This is the exact same as Challenge 122 but with a slightly less efficient solution
#I did this and 122 because they were both listed as separate challenges.

def digital_root(num):
    dig = num
    print(dig)
    while dig >= 10:
        dig_splt = [int(x) for x in str(dig)]
        print_num = 0
        print_num = sum(dig_splt)
        print(print_num)
        dig = print_num
    return


digital_root(1073741824)
raw_input()