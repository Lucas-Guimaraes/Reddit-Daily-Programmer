# https://www.reddit.com/r/dailyprogrammer/comments/5961a5/20161024_challenge_289_easy_its_super_effective/

#keeps track of all types
type_lst = ['normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting', 'poison', 'ground', 'flying', 'psychic',
            'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy']

#dictionaries for the type advantages
# x2
super_effective = {
    'fire': [type_lst[4], type_lst[5], type_lst[11], type_lst[16]],
    'water': [type_lst[1], type_lst[8], type_lst[12]],
    'electric': [type_lst[2], type_lst[9]],
    'grass': [type_lst[2], type_lst[8], type_lst[12]],
    'ice': [type_lst[4], type_lst[8], type_lst[9], type_lst[14]],
    'fighting': [type_lst[0], type_lst[5], type_lst[12], type_lst[15], type_lst[16]],
    'poison': [type_lst[4], type_lst[17]],
    'ground': [type_lst[1], type_lst[3], type_lst[7], type_lst[12], type_lst[16]],
    'flying': [type_lst[4], type_lst[6], type_lst[11]],
    'psychic': [type_lst[6], type_lst[7]],
    'bug': [type_lst[4], type_lst[10], type_lst[15]],
    'rock': [type_lst[1], type_lst[5], type_lst[9], type_lst[11]],
    'ghost': [type_lst[10], type_lst[13]],
    'dragon': [type_lst[14]],
    'dark': [type_lst[10], type_lst[13]],
    'steel': [type_lst[5], type_lst[12], type_lst[17]],
    'fairy': [type_lst[6], type_lst[14], type_lst[15]]
}

# 1/2
not_very_effective = {
    'normal': [type_lst[12], type_lst[16]],
    'fire': [type_lst[1], type_lst[2], type_lst[12], type_lst[14]],
    'water': [type_lst[2], type_lst[4], type_lst[14]],
    'electric': [type_lst[3], type_lst[4], type_lst[14]],
    'grass': [type_lst[1], type_lst[4], type_lst[7], type_lst[9], type_lst[11], type_lst[14], type_lst[16]],
    'ice': [type_lst[1], type_lst[2], type_lst[5], type_lst[16]],
    'fighting': [type_lst[7], type_lst[9], type_lst[10], type_lst[11], type_lst[17]],
    'poison': [type_lst[7], type_lst[8], type_lst[12], type_lst[13], ],
    'ground': [type_lst[4], type_lst[11]],
    'flying': [type_lst[3], type_lst[12], type_lst[16]],
    'psychic': [type_lst[10], type_lst[16]],
    'bug': [type_lst[1], type_lst[6], type_lst[7], type_lst[9], type_lst[13], type_lst[16], type_lst[17]],
    'rock': [type_lst[6], type_lst[8], type_lst[16]],
    'ghost': [type_lst[15]],
    'dragon': [type_lst[16]],
    'dark': [type_lst[10], type_lst[13]],
    'steel': [type_lst[1], type_lst[2], type_lst[3], type_lst[16]],
    'fairy': [type_lst[1], type_lst[7], type_lst[16]]
}

# 0
no_effect = {
    'normal': type_lst[13],
    'electric': type_lst[8],
    'fighting': type_lst[13],
    'poison': type_lst[16],
    'ground': type_lst[9],
    'psychic': type_lst[15],
    'ghost': type_lst[0],
    'dragon': type_lst[17],
}

#finds out specifically with pokemon
def pokemon_type(attack, defense):
    if ' ' in defense:
        def_split = defense.split()
        multiplier = find_multiplier(attack, def_split[0]) * find_multiplier(attack, def_split[1])
        if multiplier == 0:
            multiplier = int(multiplier)
    else:
        multiplier = find_multiplier(attack, defense)
    
    
    return str(multiplier) + "x"

#finds out the multiplier
def find_multiplier(attack, defense):
    multiplier = 1

    if attack in super_effective:
        if defense in super_effective[attack]:
            multiplier = 2
    if attack in not_very_effective:
        if defense in not_very_effective[attack]:
            multiplier = 0.5
    if attack in no_effect:
        if defense in no_effect[attack]:

            multiplier = 0
    return multiplier

#Checks if valid type
def t_check(ty):
    if ty in type_lst:
        return True
    else:
        return False

#quits the program
def quit_check(i):
    if i == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive: ").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            return True
    return False

print("Welcome to Pokemon Type Checker!")
print("This will check, with you as the attacker, how much damage you'll do to a different type")
print("As a note, for the defending portion, you can include two types")
print("For example, 'ice rock' is a valid word for defense")
print("\n Example Input:")
print("attack -> defense")
print("fire -> grass")
print("\n Example Output:")
print("2x")
print("\nFor a quick refersher, here are all the valid types:")
print("'normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting', 'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy'")
print("\n~*~----------------~*~\n")

checking_type = True
while checking_type:
    poke_move = raw_input("Please input a valid input. Don't forget '->'. 'q' to quit: ").lower().replace('.', '>')

    #checks if quit
    if quit_check(poke_move):
        break

    #checks if proper move
    if ' -> ' in poke_move:
        poke_move = poke_move.split(' -> ')
        attack, defense = poke_move[0], poke_move[1]

        #checks if multi-type
        if ' ' in defense:
            defen = defense.split()
            defen_1, defen_2 = defen[0], defen[1]
            if len(defen) > 2:
                print("{} is more types than two! Triple types don't exist (at least not yet)".format(defense))
            elif t_check(attack) and t_check(defen_1) and t_check(defen_2):
                print(pokemon_type(attack, defense))
            else:
                print("{}, {} and {} includes at least one invalid type!".format(attack, defen_1, defen_2))

        elif t_check(attack) and t_check(defense):
            print(pokemon_type(attack, defense))
        else:
            print("{} and/or {} are invalid types!".format(attack, defense))

    else:
        print("{} is not a valid input! Remember to put ' -> ' between attack and defense!".format(poke_move))
raw_input("Press Enter to exit.")

#print(find_multiplier('fire', 'grass'))

#print(pokemon_type('fire', 'grass'))
#print(pokemon_type('fighting', 'ice rock'))
#print(pokemon_type('psychic', 'poison dark'))
#print(pokemon_type('water', 'normal'))
#print(pokemon_type('fire', 'rock'))
#print(pokemon_type('ice', 'fire'))
