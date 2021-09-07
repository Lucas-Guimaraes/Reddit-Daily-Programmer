#https://www.reddit.com/r/dailyprogrammer/comments/2xoxum/20150302_challenge_204_easy_remembering_your_lines/

#Unfortunately, macbeth.txt was deleted from this challenge.

lines = open("macbeth.txt").read().splitlines()
phrase = "Eye of newt" #can be replaced with input


#Function to grab start of dialogue
first_not_dialog = lambda lines: next(i for i, line in enumerate(lines) if not line.startswith("    "))

#grabs the index for the line in phrase
index = next(i for i, line in enumerate(lines) if phrase in line)
#Grabs the start of the phrase IDX
dialog_start = index + 1 - first_not_dialog(lines[index::-1])
#Grabs the end of the phrase IDX
dialog_end = index + first_not_dialog(lines[index:])
#Finishes the phrase
dialog = lines[dialog_start:dialog_end]

#String formatting
print("\n".join(line.strip() for line in dialog))