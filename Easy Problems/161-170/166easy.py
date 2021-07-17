#https://www.reddit.com/r/dailyprogrammer/comments/27pgqv/692014_challenge_166_easy_ascii_fractal_curves/
import turtle

#Grabs the hilbert sequence for each 'a' and 'b'
def hilbert(hilbert_seq, r):
    for x in range(r):
        new_seq = ""
        for char in hilbert_seq:
            if char == "a":
                new_seq += "-bF+aFa+Fb-"
            elif char == "b":
                new_seq += "+aF-bFb-Fa+"
            else:
                new_seq += char
        hilbert_seq = new_seq
    return hilbert_seq


#Moves turtle speed; followed by forward, right, and left turns
def tur(hilbert_seq):
    turtle.speed(100)
    
    for char in hilbert_seq:
        if char == "F":
            turtle.forward(9)
        elif char == "+":
            turtle.right(90)
        elif char == "-":
            turtle.left(90)

# Introduction
print("Ascii Curve")
print("The first input will be your hilbert sequence. ''a' and 'b' are valid sequence additions to the curve")
print("The second input will be a range for how many prints")
print("\n~*~--------~*~\n")

#input
ascii = True
while ascii:
    w = raw_input("Path: ")
    r = raw_input("Range: ")
    if w.lower() == 'q' or r.lower() == 'q':
        break
    if r.isdigit():
        hil = hilbert(w, int(r))
        tur(hil)

raw_input("Press enter to exit.")