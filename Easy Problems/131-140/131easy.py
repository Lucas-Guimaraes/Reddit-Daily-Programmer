# https://www.reddit.com/r/dailyprogrammer/comments/1heozl/070113_challenge_131_easy_who_tests_the_tests/
def string_testing(mode, og, result):
    # reverse test - Tests by reversing the original to compare to the result
    if mode == 0:
        if og[::-1] == result:
            return "Good test data"
        else:
            return "Mismatch! Bad test data"

    # uppercase test - Tests by capitalizing the original.
    if mode == 1:
        if og.upper() == result:
            return "Good test data"
        else:
            return "Mismatch! Bad test data"


# put this in the input data part
print("Put in the mode, og, and result")
print("mode og result")
print("Example input & Output:")
print("Input: 0 Car raC")
print("Output: Good test data")
print("\n~*~----------------~*~\n")

#This handles how many cases
idx = int(raw_input("How many test strings?: "))
for i in range(idx):
    str_test = raw_input("Input a test string: ")
    mode, og, result = str_test.split()
    mode = int(mode)
    print(string_testing(mode, og, result))

raw_input("Press enter to exit")