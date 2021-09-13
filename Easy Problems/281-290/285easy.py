#https://www.reddit.com/r/dailyprogrammer/comments/54lu54/20160926_challenge_285_easy_cross/

def encode(numbers):
    output = ""

    for number in numbers.split():
        number = int(number)
        output += " 255" * (number//255)
        number = number % 255
        if number == 0:
            output += " 0"
        else:
            output += " " + str(number)

    return output[1:]

def decode(numbers):
    output = ""
    number = 0

    for numberPart in numbers.split():
        number += int(numberPart)

        if int(numberPart) < 255:
            output += " " + str(number)
            number = 0

    if number != 0: output += " " + str(number)

    return output[1:]

def check_num(t):
    for i in t:
        if i.isdigit() == False:
            return False
    return True

#Intro
print("Welcome to Byte Encoding/Decoding")
print("Put in a sequence of numbers with 'encoding' or 'decoding' at the beginning")
print('Output will be that sequence decoded or encoded!')
print("Example Input: encode 512 0 684 255 78 62 1714")
print("\n~*~----------------~*~\n")

#Continue Code
coding = True
while coding:
    numbers = raw_input()
    if numbers.lower() == 'q':
        break
    split_num = numbers.split()
    split_num = split_num[1:]
    split_check = check_num(split_num)
    if 'encode' in numbers and split_check:
        print(encode(' '.join(split_num)))
    if 'decode' in numbers and split_check:
        print(decode(' '.join(split_num)))

raw_input("Press Enter to exit.")


#Test Cases
#print(encode("512 0 684 255 78 62 1714"))
#result: 255 255 2 0 255 255 174 255 0 78 62 255 255 255 255 255 255 184
#print(decode(encode("512 0 684 255 78 62 1714")))
#result: 512 0 684 255 78 62 1714