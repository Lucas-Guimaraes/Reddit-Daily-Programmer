# https://www.reddit.com/r/dailyprogrammer/comments/qzil1/3162012_challenge_26_easy/
# duplicates go in second string

def dupe_string(input_str):
    no_dupe = []
    dupes = []
    input_list = list(input_str)
    prev_item = []
    prev_dupe_item = []

    for item in input_list:
        if item not in prev_item:
            no_dupe.append(item)
        elif item not in prev_dupe_item:
            dupes.append(item)
            prev_dupe_item = item
        prev_item = item
        print prev_item

    no_dupe = ''.join(no_dupe)
    dupes = ''.join(dupes)
    return (no_dupe, dupes)


string_input = raw_input("give me a string ba-by: ")
print dupe_string(string_input)
raw_input()