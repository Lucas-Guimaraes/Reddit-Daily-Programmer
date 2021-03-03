# https://www.reddit.com/r/dailyprogrammer/comments/vmblw/6262012_challenge_69_easy/


# this program takes in a title and a list and is able to format them
def table_list(title, lst):
    highest_len = len(title)
    # this calculates the highest len of all the items compared to the title
    for i in lst:
        if len(i) > highest_len:
            highest_len = len(i)

    # this prints everything for the title
    highest_len = highest_len + 2
    print('+' + ('-' * highest_len + '+'))
    side = (highest_len - len(title)) / 2
    side_space = ' ' * side
    print('|' + side_space + title + side_space + "|")
    print('+' + ('-' * highest_len + '+'))

    # this prints all the items
    for i in lst:
        side = (highest_len - len(i)) - 1
        side_space = ' ' * side
        print('| ' + i + side_space + "|")

    # this prints the ending
    print('+' + ('-' * highest_len + '+'))
    return


# this checks if the user wants to quit the program for opening 'q'
def quit_check(i):
    if i == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive: ").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            return True
    return False


print("This program takes two inputs: One is a title, the other is a list")
print("Both are strings")
print("I would show an example of the output")
print("But...")
print("That would ruin the fun of it!")

print("\n~*~----------------~*~\n")

t_list = True
quitting = False
while t_list:
    first_put = True
    while first_put:
        title = raw_input("Please put a title. 'q' to quit: ")
        quitting = quit_check(title)
        first_put = False

    if quitting:
        break

    second_put = True
    while second_put:
        lst = raw_input("Now put in a list:. 'q' to quit: ").replace(',', '').replace("'", '')
        quitting = quit_check(lst)
        lst = lst.split()
        second_put = False

    if quitting:
        break

    table_list(title, lst)

raw_input("Press enter to exit")

# table_list('Necessities', ['fairy', 'cakes', 'happy', 'fish', 'disgustipated', 'melon-balls'])
# table_list('Memes, dreams, and hype beams', ['fairy', 'ring modulator', 'tube amp', 'fire-hydrant', 'dog', 'cat'])
# probably use max to be able to make the corners
# "| " " |" for the sides
# obligatory other stuff
# piece of cake
