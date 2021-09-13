#https://www.reddit.com/r/dailyprogrammer/comments/3twuwf/20151123_challenge_242_easy_funny_plant/

def plant(people, plant):
    weeks = 1
    plants = [0] * plant
    while sum(plants) < people:
        plants = [i + 1 for i in plants]
        plants += [0] * sum(plants)
        weeks += 1
    return weeks

print("Welcome to Funny Plant")
print("Put in two digits: People, and plants")
print("Example input:")
print("15 1")
print("\n~*~----------------~*~\n")

funny_plant = True
while funny_plant:
    p = raw_input()
    if p.islower() == 'q':
        break
    p = p.split()
    if p[0].isdigit() and p[1].isdigit():
        print(plant(int(p[0]), int(p[1])))

raw_input("\nPress enter to exit.")