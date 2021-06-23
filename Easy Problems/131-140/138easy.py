# https://www.reddit.com/r/dailyprogrammer/comments/1ml669/091713_challenge_138_easy_repulsionforce/

# mass, x, y position
import math

def repulsion_force(particle_1, particle_2):
    #Mass, x position, and y position are extracted from the list
    particle_1_mass = particle_1[0]
    particle_1_xpos = particle_1[1]
    particle_1_ypos = particle_1[2]

    particle_2_mass = particle_2[0]
    particle_2_xpos = particle_2[1]
    particle_2_ypos = particle_2[2]

    #Handles getting the deltas, followed by the distance, and then the force
    deltaX = (particle_1_xpos - particle_2_xpos)
    deltaY = (particle_1_ypos - particle_2_ypos)
    distance = float((deltaX * deltaX + deltaY * deltaY) ** .5)
    force = ((particle_1_mass * particle_2_mass) / distance ** 2)
    return force


print(repulsion_force([1, -5.2, 3.8], [1, 8.7, -4.1]))
print(repulsion_force([4, 0.04, -0.02], [4, -0.02, -0.03]))
raw_input("Press enter to exit.")