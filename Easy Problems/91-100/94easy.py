# https://www.reddit.com/r/dailyprogrammer/comments/z6o4k/9012012_challenge_94_easy_elemental_symbols_in/

import re

#Periodic table
symbols = ["Ac", "Ag", "Al", "Am", "Ar", "As", "At", "Au", "B", "Ba", "Be", "Bh", "Bi",
           "Bk", "Br", "C", "Ca", "Cd", "Ce", "Cf", "Cl", "Cm", "Cn", "Co", "Cr", "Cs",
           "Cu", "Db", "Ds", "Dy", "Er", "Es", "Eu", "F", "Fe", "Fl", "Fm", "Fr", "Ga",
           "Gd", "Ge", "H", "He", "Hf", "Hg", "Ho", "Hs", "I", "In", "Ir", "K", "Kr", "La",
           "Li", "Lr", "Lu", "Lv", "Md", "Mg", "Mn", "Mo", "Mt", "N", "Na", "Nb", "Nd", "Ne",
           "Ni", "No", "Np", "O", "Os", "P", "Pa", "Pb", "Pd", "Pm", "Po", "Pr", "Pt", "Pu",
           "Ra", "Rb", "Re", "Rf", "Rg", "Rh", "Rn", "Ru", "S", "Sb", "Sc", "Se", "Sg", "Si", "Sm",
           "Sn", "Sr", "Ta", "Tb", "Tc", "Te", "Th", "Ti", "Tl", "Tm", "U", "Uuo", "Uup", "Uus", "Uut",
           "V", "W", "Xe", "Y", "Yb", "Zn", "Zr"]

#Highlight() will check for any symbols from the symbol list.
def highlight(str_inp):
    for sym in symbols:
        sym_lower = sym.lower()
        str_lower = str_inp.lower()
        str_temp = str_inp
        if sym_lower not in str_lower:
            continue
        variations = [str_temp[:sy.start()] + '[{}]'.format(sym) + str_temp[sy.end()+1:] for sy in re.finditer(sym_lower, str_lower)]

        for v in variations:
            print v


#Loops until user quits
elements = True
while elements:
    high = raw_input("Insert your word: ")
    #Quit case.
    if high == "q" or high == "Q":
        break
    highlight(high)

raw_input("Press enter to exit.")

#Test cases
# highlight('dailyprogrammer')
# highlight('lucasguimaraes')