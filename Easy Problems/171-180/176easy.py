# https://www.reddit.com/r/dailyprogrammer/comments/2eajf7/8222014_challenge_176_easy_pivot_table/
# 176easy.txt is a supplementary file

data_file = '176easy.txt'
farm_file = []

with open(data_file) as f:
    for line in f:
        tower, day, kwh = line.strip().split()
        farm_data = (tower, day, kwh)
        farm_file.append(farm_data)

day_week_lst = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days_of_week = {'Mon': [],
                'Tue': [],
                'Wed': [],
                'Thu': [],
                'Fri': [],
                'Sat': [],
                'Sun': []}

def format(str):
    if len(str) == 3:
        return " {} |".format(str)
    else:
        return "{} |".format(str)

def farm_pivot():
    for k in days_of_week.keys():
        for i in range(1000, 1010):
            total = 0
            for x in farm_file:
                if x[0] == str(i) and x[1] == k:
                    total += int(x[2])
            days_of_week[k].append(total)

    tower = [str(i) for i in range(1000, 1010)]
    print("Tower | Mon | Tue | Wed | Thu | Fri | Sat | Sun |")
    print("-------------------------------------------------")

    for i in range(10):
        pk = tower[i] + "  |"
        for k in day_week_lst:
            pk += format(str(days_of_week[k][i]))
        print pk

farm_pivot()
raw_input("Press enter to exit.")