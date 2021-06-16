# https://www.reddit.com/r/dailyprogrammer/comments/3wdm0w/20151209_challenge_244_easyer_array_language_part/
# https://www.kite.com/python/answers/how-to-call-a-function-by-its-name-as-a-string-in-python

# this will calculate the sum of all numbers
def sum(y, x=None):
    return reduce(lambda x, y: x + y, y if x is None else y + x)


# this will divide Y by X
def divide(y, x=None):
    if x == None:
        return y
    else:
        return y / x


# this will count the amount of items in Y (or Y + X)
def count(y, x=None):
    if x == None:
        return len(y)
    else:
        return len(y + x)


# this will implement all of the arrays
def fork(*args):
    def f(y, x=None):

        if len(args) == 3:
            return args[1](args[0](y, x), args[2](y, x))

        elif len(args) > 3 and len(args) % 2 == 1:
            return args[1](args[0](y, x), fork(*args[2:])(y, x))

    return f


def if_valid(str_put):
    total = str_put.count('count') + str_put.count('divide') + str_put.count('sum')
    list_test = (str_put[str_put.find("["):str_put.find("]")])



    if str_put[0:4] == 'fork' and total % 2 == 1:
        return True
    else:
        return False


print("Hello! Welcome to Array Language!")
print("I want you to input your function like this:")
print("fork(sum, divide, count)([1, 2, 3, 4, 5])")
print("You can do as many actions as you want with fork, as long as they are odd, followed by a list.")
print("Come on now. You try:")

print("\n~*~----------------~*~\n")

test_put = True

# this tests our input
while test_put:
    forkraw_input = raw_input("Please put in a usable action: ")
    check = if_valid(forkraw_input)
    if check is True:
        test_put = False

result = eval(forkraw_input)
print(result)

raw_input("Press enter to exit.")

