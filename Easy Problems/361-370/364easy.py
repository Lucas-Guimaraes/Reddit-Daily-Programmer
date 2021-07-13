# https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/

from random import randint


def dice_roller(amt, sides):
    total = 0
    rolls = []
    for i in range(amt):
        store = randint(1, sides)
        total += store
        rolls.append(str(store))

    rolls = ' '.join(rolls)
    return "{0}: {1}".format(total, rolls)


print("Welcome to dice!")
print("Example input:")
print("3d12")
print("Example output:")
print("12: 4, 3, 5")
print("\n~*~----------------~*~\n")

rolling = True

while rolling:
    roll = raw_input().lower()
    if roll == 'q':
        break
    split_roll = roll.split('d')
    if len(split_roll) == 2 and split_roll[0].isdigit() and split_roll[1].isdigit():
        print(dice_roller(int(split_roll[0]), int(split_roll[1])))

raw_input("Press enter to exit.")

#test case
#print(dice_roller(4, 12))