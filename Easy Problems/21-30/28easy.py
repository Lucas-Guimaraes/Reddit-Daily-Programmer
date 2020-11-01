#https://www.reddit.com/r/dailyprogrammer/comments/r59kk/3202012_challenge_28_easy/
#this application finds the first set of duplicates in an array/list

def dupe(items):
    seen = set()
    for element in items:
        if element in seen:
            yield element
        else:
            seen.add(element)
            
def first_dup(items):
    try:
        return dupe(items).next()
    except StopIteration:
        return None

list_length = int(raw_input("How long do you want your list to be?: "))
item_list = []

for i in range(list_length):
    item_list.append(int(raw_input("Please put in an item for your list: ")))
print item_list
print first_dup(item_list)
raw_input()