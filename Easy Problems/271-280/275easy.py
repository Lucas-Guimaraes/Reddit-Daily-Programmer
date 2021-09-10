#https://www.reddit.com/r/dailyprogrammer/comments/4savyr/20160711_challenge_275_easy_splurthian_chemistry/

#Function to check if valid element
def splurthian_chem(element, symbol):
    #Lowercase, find first ele, then check if second ele is in after
    element, symbol = element.lower(), symbol.lower()
    sy = element.find(symbol[0])
    check = symbol[1] in element[sy+1:]

    #If 2nd ele and 1st ele are present
    if check and sy >= 0:
        return True
    else:
        return False

#Intro
print("Welcome to Splurthian Chem")
print("Put in an element and a symbol and we will check whether it is available on this periodic table.")
print("Example Input:")
print("Spenglerium, Ee")
print("\n~*~----------------~*~\n")

#Run code
checking = True
while checking:
    chem = raw_input()
    if chem.lower() == 'q':
        break
    if ',' in chem:
        e, s = chem.replace(' ', '').split(',')
    else:
        e, s = chem.replace(' ', '').split('')
    print(splurthian_chem(e, s))

#Exit message
raw_input("Press Enter to exit.")