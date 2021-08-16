#https://www.reddit.com/r/dailyprogrammer/comments/7s888w/20180122_challenge_348_easy_the_rabbit_problem/

#Starts class
class Rabbit():
    rabbits = []
    dead_rabbits = 0

    #Initializes each rabbit
    def __init__(self, age, sex, count):
        self.age = age
        self.sex = sex
        self.count = count
        Rabbit.rabbits.append(self)

    #Handles the aging process
    def Age(self):
        self.age += 1
        if self.age == 96:
            Rabbit.dead_rabbits += self.count
            Rabbit.rabbits.remove(self)

    #Reproduction for female rabbits
    def Reproduce(self):
        if self.sex == 'F' and self.age >= 4:
            Rabbit(-1, 'F', 9 * self.count)
            Rabbit(-1, 'M', 5 * self.count)

#Counts all rabbits
def Count_All():
    count = 0
    for rabbit_pop in Rabbit.rabbits:
        count += rabbit_pop.count
    return count

#Intro Code
print("Welcome to Rabbits!")
print("Example Input:")
print("2 4 10000000")
print("First digit is the amount of male rabbits")
print("Second is the amount of female rabbits")
print("Third is the amount they need to reach to take over the world.")
print("\n~*~----------------~*~\n")


#Continue Code
rabbits_the_world = True
while rabbits_the_world:
    r = raw_input("Put in your rabbit statistics: ")

    #Checks quit code
    if r == 'q':
        break
    r = r.split()

    #Checks if input is valid
    if len(r) == 3:
        if r[0].isdigit() and r[1].isdigit() and r[2].isdigit():
            #Initializes input; makes rabbits
            m, f, total = int(r[0]), int(r[1]), int(r[2])
            Rabbit(2, 'M', m)
            Rabbit(2, 'F', f)
            months = 0

            #Counts all rabbits; checks if equal to total
            while Count_All() < total:
                for rabbit_pop in Rabbit.rabbits:
                    Rabbit.Reproduce(rabbit_pop)
                    Rabbit.Age(rabbit_pop)

                months += 1
            #Print
            print('{} Months needed to make \n'
                  '{} Hares, thus taking over the world.  \n'
                  '{} Rabbits died for this cause'.format(months, Count_All(), Rabbit.dead_rabbits))

            break

raw_input("Press enter to exit.")


#Test cases
#Rabbit(2, 'M', 1)
#Rabbit(2, 'F', 4)

#total = 1000000000000