# https://www.reddit.com/r/dailyprogrammer/comments/1sob1e/121113_challenge_144_easy_nuts_bolts/

def price_comparison():
    purchase = int(raw_input("How many items are you buying today?: "))

    #Each of these involve an enter with an item and number
    old = {k: int(v) for k, v in
           [raw_input('Old value for item {}: '.format(str(i))).split() for i in range(1, purchase + 1)]}
    new = {k: int(v) for k, v in
           [raw_input('New value for item {}: '.format(str(i))).split() for i in range(1, purchase + 1)]}
    changes = {}

    #Checks if there are any price changes
    for k, v in new.items():
        if v == old[k]:
            continue
        elif v > old[k]:
            changes[k] = '+' + str(v - old[k])

        else:
            changes[k] = '-' + str(old[k] - v)

    for k, v in changes.items():
        print('{0} {1}'.format(k, v))

    return
price_comparison()
raw_input("Press enter to exit.")