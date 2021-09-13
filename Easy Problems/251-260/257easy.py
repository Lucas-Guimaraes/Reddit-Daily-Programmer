#https://www.reddit.com/r/dailyprogrammer/comments/49aatn/20160307_challenge_257_easy_in_what_year_were/

import csv

def most_frequent(lst):
    final_lst = []
    highest = max(set(lst), key=lst.count)

    for i in range(min(lst), max(lst)+1):
        if lst.count(highest) == lst.count(i):
            final_lst.append(i)
    return final_lst

year_lst = []

with open('257presidents.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        birth_year = row[1].split()
        birth_year = int(birth_year[2])
        death_year = row[3].split()

        if death_year == []:
            death_year = 2016
        else:
            death_year = int(death_year[2])

        for year in range(birth_year, death_year+1):
            year_lst.append(year)

print(most_frequent(year_lst))