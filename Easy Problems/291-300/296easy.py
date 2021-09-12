# https://www.reddit.com/r/dailyprogrammer/comments/5j6ggm/20161219_challenge_296_easy_the_twelve_days_of/

def twelve_days():
    #Lst #1 fornames, #2 for ordinal, #3 each gift, #4 list to print each time 
    num_lst = ["A", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve"]
    each_lst = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eigth", "Ninth", "Tenth",
                "Eleventh", "Twelth"]
    gift_lst = ["Partridge in a Pear Tree", "Turtle Doves", "French Hens", "Calling Birds", "Golden Rings",
                "Geese a Laying", "Swans a Swimming", "Maids a Milking", "Ladies Dancing", "Lords a Leaping",
                "Pipers Piping", "Drummers Drumming"]
    extra_lst = []

    #For each of the twelve days of christmas
    for i in range(12):
        print("\nOn the {} day of Christmas\nmy true love sent to me:".format(each_lst[i]))
        gift = num_lst[i] + " " + gift_lst[i]
        if i == 0:
            print("A Partridge in a Pear Tree")
            extra_lst.append("and " + gift)
            continue
        else:
            extra_lst.append(gift)
            for e in extra_lst[::-1]:
                print(e)

twelve_days()
raw_input("\nPress enter to exit.")