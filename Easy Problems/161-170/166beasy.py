# https://www.reddit.com/r/dailyprogrammer/comments/284mep/6142014_challenge_166b_easy_planetary_gravity/

from math import pi

#calculates the force in the planet
def planet(mass_1, radius, density):
    gravity = 6.67e-11
    volume = (4 * pi * radius ** 3) / 3
    mass_2 = volume * density
    force = gravity * ((mass_1 * mass_2) / (radius ** 2))
    return round(force, 3)

# Introduction
print("Planetary gravity: First input will be the mass of an object")
print("The second will be how many planets")
print("The third will calculate for every planet")
print("\n~*~--------~*~\n")

#input
galaxy = True
while galaxy:
    print_lst = []
    mass_1 = raw_input("Mass: ")
    planet_amt = raw_input("Number of Planets: ")
    
    #quit case for first two inputs
    if mass_1.lower() == 'q' or planet_amt.lower() == 'q':
        break
    
    #Checks if inputs are both digits
    if (mass_1.isdigit()) and planet_amt.isdigit():
        
        #For each amount
        for i in range(int(planet_amt)):
            
            #Gets third input, splits name, radius, and density
            prd = raw_input("Planet, Radius, Density: ")
            prd = prd.split(',')
            prd = [p.replace(" ", "") for p in prd]
            planet_name, radius, density = prd[0], prd[1], prd[2]
            
            #Split digits
            if radius.isdigit() and density.isdigit():
            
                #gets force, adds format, add to print list
                force = planet(int(mass_1), int(radius), int(density))
                p = "{}: {}".format(planet_name, force)
                print_lst.append(p)
                
        #print each one in list
        for p in print_lst:
            print(p)

raw_input("Press enter to exit.")