#https://www.reddit.com/r/dailyprogrammer/comments/7hhyin/20171204_challenge_343_easy_major_scales/

#Solfege index, chromatic scale
sol_idx = {'Do': 0, 'Re': 1, 'Mi': 2, 'Fa': 3, 'So': 4, 'La': 5, 'Ti': 6}
chrom_scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def note(key, sol):
    idx = sol_idx[sol]
    cur = chrom_scale.index(key)
    major_steps = [2, 2, 1, 2, 2, 2, 0]
    major_lst = []
    for i in range(7):
        if cur > 11:
            cur -= 12
        major_lst.append(chrom_scale[cur])
        cur += major_steps[i]
        if idx+1 == len(major_lst):
            return major_lst[-1]

#Input
print("Welcome to note!")
print("Give a key and a solfege (Do, Re, Mi, Fa, So, La, Ti)")
print("And this will return the result.")

print("\n~*~----------------~*~\n")

#Run code
theory = True
while theory:
    n = raw_input()
    if n.lower() == 'q':
        break
    key, sol = n.split()
    key, sol = key.upper(), sol.capitalize()
    if key in chrom_scale and sol in sol_idx.keys():
        print(note(key, sol))

print("Press enter to exit")

#Test case:
#print(note("C", "Do"))
#print(note("C", "Re"))
#print(note("C", "Mi"))
#print(note("D", "Mi"))
#print(note("A", "Fa"))