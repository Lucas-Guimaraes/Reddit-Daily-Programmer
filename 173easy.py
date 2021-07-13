# https://www.reddit.com/r/dailyprogrammer/comments/2bxntq/7282014_challenge_173_easy_unit_calculator/

# Hogsheads is of beryllium
#Dictionary for units and type list for checking
units = {
    'meters': ('length', 1),
    'inches': ('length', 39.3701),
    'attoparsecs': ('length', 32.4077929),
    'miles': ('length', 0.000621371),
    'kilograms': ('mass', 440.7),
    'pounds': ('mass', 971.6),
    'ounces': ('mass', 15550),
    'hogsheads': ('mass', 1)
}

types = units.keys()

#checks if float
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


#converts
def conversion(num, og, new):
    #
    og_type, new_type, og_msure, new_msure = units[og][0], units[new][0], units[og][1], units[new][1]

    #checks which is bigger
    if og_type == new_type:
        result = num * (new_msure / og_msure)
  # quit case
    else:
        return '{} and {} can not be matched'.format(og, new)

    # checks if hogsheads is contained for proper conversion
    if og == 'hogsheads':
        og = 'hogsheads'
    elif new == 'hogsheads':
        new = 'hogsheads:'
    return '{} {} is {} {}'.format(num, og, result, new)


print("Welcome to Length and Mass Converter!")
print("Example input:")
print("3 meters to inches")
print("Example output:")
print("3 meters is 118.1 inches")
print("Usable Length definers: meters, inches, attoparsecs, miles")
print("Usable Mass definers: kilograms, pounds, ounces, hogsheads")
print("\n~*~----------------~*~\n")

converting = True

while converting:
    form = raw_input().lower()
    if form == 'q':
        break
    split_form = form.split()
    if len(split_form) == 4:
        if (split_form[0].isdigit() or isfloat(split_form[0])) and split_form[1] in types and split_form[3] in types:
            print(conversion(float(split_form[0]), split_form[1], split_form[3]))

raw_input("Press enter to exit.")