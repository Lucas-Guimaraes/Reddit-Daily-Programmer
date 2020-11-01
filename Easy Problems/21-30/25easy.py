#https://www.reddit.com/r/dailyprogrammer/comments/qxuug/3152012_challenge_25_easy/

def elections(lst):
    victory_number = 0
    count_index = -1
    for item in lst:
        count_index += 1
        candidates_votes = int(item)
        if candidates_votes > victory_number:
            victory_number = candidates_votes
            victory_index = count_index
    count_index = -1
    
    for item in lst:
        count_index += 1
        if lst[count_index] == lst[victory_index] and victory_index != count_index:
            tie_index = count_index
            tie_candidate = lst[count_index]
            return "The election is a tie. The winners are candidate %s and %s. They both received %s votes." % (victory_index+1, tie_index+1, victory_number)
    return "The winner is %s. They received %s votes." % (victory_index+1, victory_number)


candidates = int(raw_input("How many candidates are there?: "))
candidate_lst = []
for i in range(1, candidates+1):
    item = int(raw_input("How many votes did candidate %s receive?: " % i))
    candidate_lst.append(item)

print elections(candidate_lst)
raw_input()