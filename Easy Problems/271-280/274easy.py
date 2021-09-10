#https://www.reddit.com/r/dailyprogrammer/comments/4r8fod/20160704_challenge_274_easy_gold_and_treasure_the/

#Handles the declaration
declaration = open("274easydeclaration.txt", "r")
declaration = declaration.read()
declaration = declaration.split()

#Handles the numbers/index points
numbers = open("274easynumbers.txt", "r")
numbers = numbers.read()
numbers = numbers.replace(",", "")
numbers = numbers.split()

#Deciphering
decipher = []
for n in numbers:
    decipher.append(declaration[int(n)-1][0])
decipher = "".join(decipher)

print(decipher)