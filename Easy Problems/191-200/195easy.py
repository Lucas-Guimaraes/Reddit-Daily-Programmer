# https://www.reddit.com/r/dailyprogrammer/comments/2qmz12/20141228_challenge_195_easy_symbolic_link/

#splits all of them by :, then updates the dictionary
#the first half is the key, while the second half is the value
def updateDict(rawInput):
    splitInput = rawInput.split(":")
    symDict.update({trimSlash(splitInput[0]):
                        trimSlash(splitInput[1])})

#also trips all slashes as necessary
def trimSlash(input):
    if input[-1] == r"/":
        return input[:-1]
    else:
        return input

#This checks how many links the user would like to have
#followed by adding every link to our dictionary
def readInput():
    numberOfLinks = raw_input("Enter the number of links:\n")
    for i in range(int(numberOfLinks)):
        updateDict(raw_input("Enter link:\n"))

#this handles the input for our actual path
def walkInput(userInput):
    splitInput = userInput.split(r"/")
    curPath = ""
    #this whole part handles our current path
    #first, we join all parts in Split Input to the path
    #Then, we get it from our dictionary
    #Finally, return the current pathway
    for part in splitInput:
        if len(part): curPath = r"/".join((curPath, part))
        curPath = symDict.get(curPath, curPath)
    if curPath != userInput: curPath = walkInput(curPath)
    return curPath


symDict = {}
readInput()
outPath = walkInput(raw_input("Enter the path to be expanded:\n"))
print "The expanded path is:\n" + outPath