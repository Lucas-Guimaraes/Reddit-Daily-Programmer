#https://www.reddit.com/r/dailyprogrammer/comments/2q2xnc/20141222_challenge_194_easy_destringification/

#Keys to value converter
esc = {
	"\\\"": '\"',
	"\\n":  '\n',
	"\\\'": '\'',
	"\\\?": '\?',
	"\\\\": '\\',
	"\\a": '\a',
	"\\b": '\b',
	"\\f": '\f',
	"\\n": '\n',
	"\\r": '\r',
	"\\t": '\t',
	"\\v": '\v'
}
#List of keys
esc_keys = esc.keys()

#Program to check strings
def destring(sen):
    #IV will be used for every time a string is not valid
    iv = "Invalid string"

    #Checks if valid enclousre for string
    if sen[0] == "\"" and sen[-1] == "\"":
        sen = sen[1:len(sen)-1]
    else:
        return iv

    #Replaces all keys to values
    no_fault = True
    while no_fault:
        for e in esc_keys:
            if e in sen:
                sen = sen.replace(e, esc[e])
        else:
            no_fault = False

    #Checks if quit cases are valid
    for i in range(len(sen)):
        tmp = ""
        if sen[i] == "\\":
            #Checks if string closes
            if i+1 >= len(sen):
                return iv
            else:
                tmp += sen[i] + sen[i+1]
                # Checks values
                if tmp not in esc:
                    return iv

    return sen

#Input
print("Welcome to Destringification?...")
print("This program will tell you if what you have inserted is a valid string")
print("\n~*~----------------~*~\n")

#Run Code

destringing = True

while destringing:
    d = raw_input()
    if d.lower() == "q":
        break
    print(destring("\"{}\"".format(d[1:len(d) - 1])))

raw_input("Press enter to exit.")
#test case
#c = raw_input()
#print(destring("\"{}\"".format(c[1:len(c)-1])))

