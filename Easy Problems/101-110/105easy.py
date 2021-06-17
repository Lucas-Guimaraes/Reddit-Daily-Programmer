# https://www.reddit.com/r/dailyprogrammer/comments/11shra/10202012_challenge_105_easy_word_unscrambler/

#This program comes with a lot of supplementary files

#105easy-lowercase.py will make all the text in 105easy-test-lower.txt lowercase
#105easy-test-scrambled.txt is the original scrambled file. the .py file will rescramble them all
#105easy-shuffled.txt is just a saved version from before. It is the version this program uses, but you are welcome to change it to 105easy-test-scrambled.txt


from random import shuffle

#creates our dictionary
def create_dict(unscrambled, scrambled):
    unscramble = open(unscrambled, "r")
    scramble = open(scrambled, "r")
    unshuffled = {}
    
    #for every word, we strip them all
    #If they have the same set, we add it to the unscrambled dictionary
    for word in scramble.readlines():
        word = word.strip()
        unscramble.seek(0)
        for unscram in unscramble.readlines():
            unscram = unscram.strip()
            if set(unscram) == set(word):
                unshuffled[unscram] = word
                
    #We print out the results of the dictionary here
    for k, v in sorted(unshuffled.items()):
        print(k + " : " + v)
    unscramble.close()
    scramble.close()
create_dict("105easy-test-lower.txt", "105easy-test-shuffled.txt")

#This input is just to press enter to exit.
raw_input()