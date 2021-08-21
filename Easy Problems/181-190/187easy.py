my_input = \
'''
a:all
f:force
n:networking
N:numerical-list
-aN 12 --verbose 192.168.0.44'''

try:
	my_input = sys.argv[1]
except:
	pass

my_input = my_input.split('\n')

#Grabs Flags
flags = dict([x.split(':') for x in my_input[1:-1]])

#grabs identifiers
for word in my_input[-1].split(' '):
	#Grabs Parameters
	if word[0] != '-':
		print('parameter: ' + word)

	#Grabs Flags
	elif word[1] !='-':
		for char in word[1:]:
			print('flag: ' + flags[char])

	#Grabs any flags designated with '--'
	else:
		print ('flag: ' + word)

raw_input("Press enter to exit.")