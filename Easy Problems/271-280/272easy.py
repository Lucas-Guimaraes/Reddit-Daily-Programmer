# https://www.reddit.com/r/dailyprogrammer/comments/4oylbo/20160620_challenge_272_easy_whats_in_the_bag/
# http://scrabblewizard.com/scrabble-tile-distribution/

#All tiles
all_tiles = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2,
             'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1,
             '_': 2}



#Starts up scrabble
def scrabble():
    scrabble_game = True
    tiles = all_tiles.copy()
    
    #while playing the game
    while scrabble_game:
        valid_word = True
        previous_state = tiles.copy()
        word = raw_input("Give a word:\n").upper()
        
        #checks to see if a letter is still in the bag
        for w in word:
            tiles[w] = tiles[w] - 1
            if 0 > tiles[w]:
                tiles = previous_state.copy()
                print("Invalid input. More {}'s have been taken from the bag than possible.".format(w))
                valid_word = False
    
        #if the word is valid, print the bag in reversed
        bag = {}
        if valid_word:
            for k, v in tiles.iteritems():
                bag[v] = bag.get(v, []) + [k]
            for k in reversed(bag.items()):
                print(k)

        #if all the tiles are used, break the game loop
        if sum(tiles.values()) == 0:
            break
    
    #checks if the user wants to play again
    restart = raw_input("Restart? y for yes, any other input to break")
    if restart == 'y':
        scrabble()

scrabble()
raw_input("Press enter to exit")