# https://www.reddit.com/r/dailyprogrammer/comments/341c03/20150427_challenge_212_easy_r%C3%B6varspr%C3%A5ket/

def rovarspraket(w):
    consonants = "bcdfghjklmnpqrstvwxyz"
    rovar_w = ''
    for l in w:
        if l in consonants:
            rovar_w += l + 'o' + l
        else:
            rovar_w += l
    return rovar_w


print("Welcome to Robber's Language!")
print("Input a string, get back the word")
print("\n~*~----------------~*~\n")

rovar = True

while rovar:
    word = raw_input()
    if word == 'q' or word == 'Q':
        break
    print(rovarspraket(word))

raw_input("Press enter to exit.")

# test cases
# print(rovarspraket("I'm speaking Robber's language!"))