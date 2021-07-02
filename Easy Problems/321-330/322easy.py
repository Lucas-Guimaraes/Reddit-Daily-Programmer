# https://www.reddit.com/r/dailyprogrammer/comments/6l3hd8/20170703_challenge_322_easy_all_pairs_test/

#To use 'product' to grab all combinations, and 'combinations' to grab pairs.
import itertools

#Checks all the pairs in all sublists
def pairs(lsts):
    #Gets ALL combinations
    group = list(itertools.product(*lsts))

    #Cur_pairs is our duplicate checker. Final_pairs makes sure no duplicate pairs get delivered
    cur_pairs = []
    final_pairs = []

    #for every item in all combinations
    for i in group:
        new_lst = []
        new_lst = itertools.combinations(i, 2)

        #iterates through the combinations from the group item
        for new in new_lst:
            #if the combination is new, it is added
            if new not in cur_pairs:
                cur_pairs.append(new)
                #Checks to see if the pair is in the final list
                if i not in final_pairs:
                    final_pairs.append(i)

    return len(final_pairs)

#test case
print(pairs([['0', '1'], ['A', 'B', 'C'], ['D', 'E', 'F', 'G']]))