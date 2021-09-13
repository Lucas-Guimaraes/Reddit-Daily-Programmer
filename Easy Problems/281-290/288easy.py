#https://www.reddit.com/r/dailyprogrammer/comments/57zcbm/20161017_challenge_288_easy_detecting_alliteration/

#Detecting Alliteration
stop_words = ["i", "a", "about", "an", "and", "are", "as", "at",
              "be", "by", "com", "for", "from", "how", "in", "is",
              "it", "of", "on", "or", "that", "the", "this", "to",
              "was", "what", "when", "where", "who", "will", "with",
              "the"]
def alliteration(sentence):

    allit_lst = []
    words = sentence.split()
    words = [w.lower() for w in words if w.lower() not in stop_words]
    for number, w in enumerate(words):
        #Cur, previous indexes
        cur = words[number][0].lower()
        prev = words[number - 1][0].lower()
        #Used to take away non alpha letters
        w = [i for i in w if i.isalpha()]
        w = ''.join(w)
        w_check = w not in allit_lst

        #if we are on the last IDX
        if number == len(words)-1:
            if prev == cur and w_check:
                allit_lst.append(w)
        else:
            #Next idx, which can not be made if we are on the last IDX.
            next = words[number+1][0].lower()
            if (next == cur or prev == cur) and w_check:
                allit_lst.append(w)
    return ' '.join(allit_lst)

#Intro
print("Welcome to Alliteration")
print("Put in a phrase, and we will get out all the alliterative letters")
print("\n~*~----------------~*~\n")

#Continue Code
alliterating = True
while alliterating:
    sentence = raw_input()
    if sentence.lower() == 'q':
        break
    print(alliteration(sentence))

raw_input("Press Enter to exit.")

#Test Cases
#print(alliteration('Peter Piper Picked a Peck of Pickled Peppers'))
#print(alliteration('Bugs Bunny likes to dance the slow and simple shuffle'))
#print(alliteration("You'll never put a better bit of butter on your knife"))
#print(alliteration("The daily diary of the American dream"))
#print(alliteration("For the sky and the sea, and the sea and the sky"))
#print(alliteration("Three grey geese in a green field grazing, Grey were the geese and green was the grazing."))
#print(alliteration("But a better butter makes a batter better."))
#print(alliteration("His soul swooned slowly as he heard the snow falling faintly through the universe and faintly falling, like the descent of their last end, upon all the living and the dead."))
#print(alliteration("Whisper words of wisdom, let it be."))
#print(alliteration("They paved paradise and put up a parking lot."))
#print(alliteration("So what we gonna have, dessert or disaster?"))