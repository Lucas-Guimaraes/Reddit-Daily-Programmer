# https://www.reddit.com/r/dailyprogrammer/comments/3s4nyq/20151109_challenge_240_easy_typoglycemia/
import re
import random

# typo = typoglycemia - gets the typo word
#scrambles each found word
def typo_word(word):
    last = len(word) - 1
    ran_w = list(word[1:last])
    random.shuffle(ran_w)
    ran_w = ''.join(ran_w)
    return word[0] + ran_w + word[last]

#decides whether the word needs to be scrambled randomly (5 letters or more) or not
def scramble(match):
        word = match.group()
        if len(word) < 4:
            return word
        elif len(word) == 4:
            return word[0] + word[2] + word[1] + word[3]
        else:
            return typo_word(word)

#Returns paragraph, uses Scramble for each found word
def typo_paragraph(para):
    return re.sub(r'[A-Za-z]+', scramble, para)

print("Welcome to typoglycemia")
print("Put in a paragraph, and we will shuffle all of the middle letters")
print("\n~*~----------------~*~\n")

shuffling = True
while shuffling:
    paragraph = raw_input()
    #quit code
    if paragraph.lower() == 'q':
        break

   print(typo_paragraph(paragraph))

raw_input("Press enter to exit.")

#test cases
#print(typo_paragraph("That"))
#print(typo_paragraph("""According to a research team at Cambridge University, it doesn't matter in what order the letters in a word are, 
#the only important thing is that the first and last letter be in the right place. 
#The rest can be a total mess and you can still read it without a problem.
#This is because the human mind does not read every letter by itself, but the word as a whole. 
#Such a condition is appropriately called Typoglycemia."""))
#print(typo_paragraph("According to all known laws of"))