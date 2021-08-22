# https://www.reddit.com/r/dailyprogrammer/comments/34rxkc/20150504_challenge_213_easy_pronouncing_hex/

# Phrases
phrases = {'0': "Bitey",
           '1': "Eleventy",
           '2': "Twenty",
           '3': "Thirty",
           '4': "Fourty",
           '5': "Fifty",
           '6': "Sitxy",
           '7': "Seventy",
           '8': "Eighty",
           '9': "Ninety",
           'A': "Atta",
           'B': "Bibbity",
           'C': "City",
           'D': "Dickety",
           'E': "Ebbity",
           'F': "Fleventy"}


# Function to actually pronounce hex
def pronounce_hex(hex):
    final = ""
    hex_cut = hex[2:]

    # For each item in the cut hex
    for i in range(len(hex_cut)):

        # If beginning, don't bother adding a space or '-'
        if i == 0:
            final += phrases[hex_cut[i]]
            continue

        # Checks whether to add a '-' or ' '
        if i % 2 != 0:
            final += "-"
        elif i != hex_cut:
            final += " "

        # Adds the phrase!
        final += phrases[hex_cut[i]].lower()

    # Returns final phrase!
	return final


# Input
print("Welcome to hex pronounciation!")
print("Insert a hexidecimal and this will give you the result")

print("\n~*~----------------~*~\n")

# Run code
hexing = True
while hexing:
	p_hex = raw_input()
	if p_hex.lower() == 'q':
		break

	print(pronounce_hex(p_hex))

print("Press enter to exit")

# Test Cases
# p_hex = "0xA0C9"
