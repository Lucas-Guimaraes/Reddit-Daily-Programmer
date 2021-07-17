# https://www.reddit.com/r/dailyprogrammer/comments/26ijiu/5262014_challenge_164_easy_assemble_this_scheme/
# 164easy.js is where the actual meat of this assignment is
# I used this to still test 'Eval'

def helloworld():
    return "Hello World"


def fizzbuzz():
    arr = []
    for i in xrange(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            arr.append(i)
    return arr


def anagram_check(a, b):
    if (sorted(a) == sorted(b)):
        return True
    else:
        return False


def remove_letter(word, letter):
    return word.replace(letter, '')


def sum_lst(lst):
    return sum(lst)


print("Your following possible functions are: ")
print("""helloworld()\n
fizzbuzz()\n
anagram_check(a, b)\n
remove_letter(word, letter)\n
sum_lst(lst)""")
print("\n~*~----------------~*~\n")
morse_seq = True

# Loop that keeps the program go until the user quits
while morse_seq:
    func = raw_input()
    if func == 'q' or func == 'Q':
        break
    print(eval(func))

raw_input("\nPress enter to exit.")
