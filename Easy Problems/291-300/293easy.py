#https://www.reddit.com/r/dailyprogrammer/comments/5e4mde/20161121_challenge_293_easy_defusing_the_bomb/

#Bad_dict will lead to game overs if there is a match
#Good_dict will lead to game overs if there is no match
#This could be simplified to one dictionary
bad_dict = {'white': ["white", "black"],
			'black': ["white", "green", "orange"],
			"purple": ["purple", "green", "orange", "white"]}

good_dict = {"red": ["green"],
			 "orange": ["red", "black"],
			 "green": ["orange", "white"]}

wires = []

print("If you cut a white cable you can't cut white or black cable.")
print("If you cut a red cable you have to cut a green one")
print("If you cut a black cable it is not allowed to cut a white, green or orange one")
print("If you cut a orange cable you should cut a red or black one")
print("If you cut a green one you have to cut a orange or white one")
print("If you cut a purple cable you can't cut a purple, green, orange or white cable")
print("")
#Runs our quit code
def explode():
	print "Boom"
	quit()

#While getting user input
while True:
	try:
		wire = raw_input()
		if wire in bad_dict.keys() or good_dict.keys():
			wires.append(wire)
	except: break

print("")
#ctrl_d to break out and see results
#Checks if invalid wire
cur = len(wires)
for i in range(1, len(wires)):
	if wires[i] in bad_dict.keys():
		if wires[i-1] in bad_dict[wires[i]]:
			explode()
	if wires[i] in good_dict.keys():
		if wires[i-1] not in good_dict[wires[i]]:
			explode()

print("Bomb defused.")