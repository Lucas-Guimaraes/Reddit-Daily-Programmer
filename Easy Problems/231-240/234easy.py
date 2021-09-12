#https://www.reddit.com/r/dailyprogrammer/comments/3moxid/20150928_challenge_234_easy_vampire_numbers/

import itertools

def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res

def vamp_split(fang, result, *kwargs):
    if fang == 2:
        v_str = "{}={}*{}".format(result, kwargs[0], kwargs[1])
    elif fang == 3:
        v_str = "{}={}*{}*{}".format(result, kwargs[0], kwargs[1], kwargs[2])
    elif fang == 4:
        v_str = "{}={}*{}*{}*{}".format(result, kwargs[0], kwargs[1], kwargs[2], kwargs[3])
    return v_str

def check_zero(fang, *kwargs):
    no_zero = True
    for i in range(fang):

        if kwargs[i] % 10 == 0:
            if no_zero:
                no_zero = False
            else:
                return False
    return True

def vampire_numbers(n, fang):
    amt = '*' * fang
    range_amt = len(str(amt))
    fang_digits = n // fang
    fang_start = 10 ** (fang_digits - 1)
    fang_stop = 10 ** fang_digits
    result_list = []
    final_list = []
    combinations = itertools.combinations_with_replacement(range(fang_start, fang_stop), fang)

    for i in combinations:
        result = prod(i)
        if result not in result_list:
            if len(str(result)) == n:
                x = [str(x) for x in i]
                x = "".join(x)
                result = [str(y) for y in str(result)]
                result = "".join(result)

                if sorted(result) == sorted(x):

                    result_list.append(result)
                    if fang == 2:
                        final_list.append(vamp_split(fang, result, i[0], i[1]))
                    elif fang == 3 and check_zero(fang, i[0], i[1], i[2]):
                        final_list.append(vamp_split(fang, result, i[0], i[1], i[2]))
                    elif fang == 4 and check_zero(fang, i[0], i[1], i[2], i[3]):
                        final_list.append(vamp_split(fang, result, i[0], i[1], i[2], i[3]))

    for f in sorted(final_list):
        print(f)

vampire_numbers(6, 3)
#vampimre_numbers(6, 3)
raw_input("Press enter to exit.")