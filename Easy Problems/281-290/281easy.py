# https://www.reddit.com/r/dailyprogrammer/comments/504rdh/20160829_challenge_281_easy_something_about_bases/

#Extra space included to stop at 17
hex_16 = "0123456789abcdef "
def check_base(c_str):
    base = hex_16.find(max(str(c_str))) + 1
    while 17 > base:

        print('base {} => {}'.format(base, int(c_str, base)))
        new_str = hex_16[base]
        base = hex_16.find(max(str(new_str))) + 1

    # base 2 => 1
check_base(("21"))