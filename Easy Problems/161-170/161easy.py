#https://www.reddit.com/r/dailyprogrammer/comments/24r50l/552014_161_easy_blackjack/

import random

#This starts up the game
def game():
    num_of_decks = raw_input('Enter the number of decks: ')
    if num_of_decks == 'q' or num_of_decks == 'Q':
        return False
    shoe = get_shoe(int(num_of_decks))
    hands = 0
    blackjacks = 0

    while len(shoe) >= 1:
        total = get_value(shoe.pop(), shoe.pop())
        hands += 1
        if total == 21:
            blackjacks += 1
    print(blackjacks)
    percent = round(float(blackjacks) / float(hands) * 100.0, 2)
    print("Among {0} hands there were {1} blackjacks at a {2} rate".format(str(hands), str(blackjacks), str(percent)))
    return True

#make all the decks for the amount of decks
def get_shoe(n_decks):
    deck = get_deck()
    shoe = []
    for i in range(n_decks):
        shoe += deck
    random.shuffle(shoe)

    return shoe

#make deck
def get_deck():
    cards = ['2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['D', 'C', 'S', 'H']
    deck = []

    for card in cards:
        for suit in suits:
            deck.append(card + suit)

    return deck

#adds card 1 and 2
def get_value(card_one, card_two):
    card_one = card_one[:-1]
    card_two = card_two[:-1]

    face_cards = {'J': '10', 'Q': '10', 'K': '10', 'A': '11'}

    if card_one in face_cards:
        card_one = face_cards[card_one]
    if card_two in face_cards:
        card_two = face_cards[card_two]
    return int(card_one) + int(card_two)

print("Input is how many hands you want to draw")
print("Output will be how many blackjacks.")
print("\n~*~----------------~*~\n")

#checks blackjack
no_escape = True
while no_escape:
    check = game()
    if check == False:
        break


raw_input("\nPress enter to exit.")