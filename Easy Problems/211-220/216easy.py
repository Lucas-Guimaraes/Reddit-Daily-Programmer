#https://www.reddit.com/r/dailyprogrammer/comments/378h44/20150525_challenge_216_easy_texas_hold_em_1_of_3/

from random import shuffle
from itertools import product
#Creates card list
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
cards = ["{} of {}".format(*hand) for hand in product(values, suits)]

#Shuffles cards
shuffle(cards)

#Deal function, burn function
deal = lambda n: [cards.pop() for _ in range(n)]
burn = cards.pop

#Asks how many players
n_players = int(input("How many players (2-8) : "))
print("")

#Sets up hands
myhand = deal(2)
print("Your hand: {}, {}".format(*myhand))
for i in range(n_players - 1):
	hand = deal(2)
	print("CPU {} hand: {}, {}".format(i+1, *hand))

#Flop, turn, and river setup
_, flop, _, turn, _, river = burn(), deal(3), burn(), deal(1), burn(), deal(1)

print("")
print("Flop: {}, {}, {}".format(*flop))
print("Turn: {}".format(*turn))
print("River: {}".format(*river))