# hhttps://www.reddit.com/r/dailyprogrammer/comments/sobna/4232012_challenge_42_easy/
# print lyrics

def beer_word(num):
    ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    lower_num = num - 1
    if num > 9:
        if num == 10:
            beer = tens[0]
        if num in range(11, 20):
            beer_index = num - 11
            beer = teens[beer_index]
        else:
            beer_list = [int(i) for i in str(num)]
            beer_list_index = [int(beer_list[0]) - 1, int(beer_list[1]) - 1]
            first_digit = tens[beer_list_index[0]]
            second_digit = ones[beer_list_index[1]]
            beer = str(first_digit) + "-" + str(second_digit)
    else:
        beer_index = num - 1
        beer = ones[beer_index].title()

    return beer


def beers_on_wall():
    for beer in reversed(range(100)):
        beer_string = beer_word(beer)
        lower_beer_string = beer_word(beer - 1)
        print(" ")
        if beer > 2:
            print(beer_string + " bottles of beer on the wall,")
            print(beer_string + " bottles of beer.")
            print("You take one down, pass it around.")
            print(lower_beer_string + " bottles of beer on the wall.")
        elif beer == 2:
            print(beer_string + " bottles of beer on the wall,")
            print(beer_string + " bottles of beer.")
            print("You take one down, pass it around,")
            print(lower_beer_string + " bottle of beer on the wall.")
        elif beer == 1:
            print("One bottle of beer on the wall,")
            print("One bottle of beer.")
            print("You take one down, pass it around,")
            print("No more bottles of beer on the wall.")

        else:
            print("No more bottles of beer on the wall,")
            print("No more bottles of beer,")
            print("Go to the store and buy some more,")
            print("So we can get 99 more bottles of beer on the wall.")
            break


def ol_mcdonald():
    animals = ['cow', 'chicken', 'turkey', 'kangaroo', 't-rex', 'road runner']
    sounds = ['moo', 'cluck', 'gobble', "G'day", 'raagh', 'meep-meep']
    for x in range(0, 6):
        print("old mc donald had a farm e-i e-i o")
        print("and on this farm he had an {}".format(animals[x]))
        print("e-i e-i o")
        print("with a {} here and a {} there.".format(sounds[x], sounds[x]))
        print("old mc donald had a farm e-i e-i o")
        print(" ")
    print("old mc donald made strange investmets in livestock e-i-e-i-o")


def christmas():
    days = ["First", "Second", "Third", "Fourth",
            "Fifth", "Sixth", "Seventh", "Eighth",
            "Ninth", "Tenth", "Eleventh", "Twelfth"]
    gifts = ["partridge in a pear tree.",
             "Two turtle doves,",
             "Three french hens,",
             "Four calling birds,",
             "Five Gold-en Riiings,",
             "Six geese-a-laying,",
             "Seven swans-a-swimming,",
             "Eight maids-a-milking,",
             "Nine ladies dancing,",
             "Ten lords-a-leaping,",
             "Eleven pipers piping,",
             "Twelve drummers drumming,"]
    # this goes through the items in both the 'gifts' list and the 'days' list
    for day in range(0, 12):
        count = day + 1
        print(" ")
        print("On the {} day of Christmas, my true love gave to me ".format(days[day]))
        for num in reversed(range(count)):
            if num == 0 and day == 0:
                print("A " + gifts[num])
            elif num == 0:
                print("And a " + gifts[num])
            else:
                print(gifts[num])

def song_choice(option):
    if option == 'a':
        beers_on_wall()
    elif option == 'b':
        ol_mcdonald()
    elif option == 'c':
        christmas()
    else:
        print("You have printed an invalid option. Goodbye.")

print("*--------*--------*")
print("Hello! Welcome to Lyrics Printer")
print("*--------*--------*")
raw_input("Press Enter to Continue")
print("*--------*--------*")
print("This application takes one input that prints out three options")
print("A) Ninety-nine bottles of beer on the wall")
print("B) Old McDonald")
print("C) 12 days of Christmas")
print("*--------*--------*")
raw_input("Press Enter to Continue")
print("*--------*--------*")
choice = raw_input("Give me a choice using 'a', 'b', or 'c'!: ")
choice = choice.lower()
song_choice(choice)
print("*--------*--------*")
raw_input("Press Enter to Exit")