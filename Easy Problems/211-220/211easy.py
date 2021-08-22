#https://www.reddit.com/r/dailyprogrammer/comments/338p28/20150420_challenge_211_easy_the_name_game/

#Makes our rhyme
vowels = ["A", "E", "I", "O", "U"]
def rhyme(word):
    if word[0] == word[1]:
        word = word[0] + "o" + "-" + word[2:]
    elif word[1] in vowels:
        word = word[0] + word[1:].lower()
    else:
        word = word[0] + word[2:]
    return word

#Plays the Name Game
def game(word):
    #removes exclamation point
    word = word[0:len(word)-1]
    #Makes F, B, and M rhymes - checks if word starts with "M, B, or
    f_rhyme, b_rhyme, m_rhyme = "F" + word, "B" + word, "M" + word
    f_rhyme, b_rhyme, m_rhyme = rhyme(f_rhyme), rhyme(b_rhyme), rhyme(m_rhyme)

    #lines
    first = f_rhyme + ", " + f_rhyme + " bo " + b_rhyme + ","
    second = "Bonana fanna fo " + f_rhyme
    third = "Fee fy mo " + m_rhyme
    fourth = word + "!"

    #Comebines all lines, prints each line.
    rhyme_lst = [first, second, third, fourth]
    for r in rhyme_lst:
        print(r)

#Input
print("Welcome to The Name game!")
print("Put in a word in the alphabet")
print("You can follow it up with a '!' at the end")
print("And this will print the rhyming version!")
print("\n~*~----------------~*~\n")

#Run Code

namegame = True

while namegame:
    w = raw_input().capitalize()
    if w.lower() == 'q':
        break
    if w[-1] != "!":
        w += "!"
    if w[0:len(w)-1].isalpha():
        game(w)


raw_input("Press enter to exit.")

#Test cases
#print(game("Lucas!"))
#print(game("Arnold!"))