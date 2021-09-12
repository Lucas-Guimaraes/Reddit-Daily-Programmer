#https://www.reddit.com/r/dailyprogrammer/comments/5llkbj/2017012_challenge_298_easy_too_many_parentheses/

def check_pairs(word):
    for i, char in enumerate(word):
        if char == '(':
            pairs.append([i, -1])
        elif char == ')':
            k = -1
            while pairs[k][1] != -1:
                k -= 1
            pairs[k][1] = i
    return pairs

def filter_pairs(pairs):
    filter_lst = []
    for i in range(len(pairs)):
        if i < len(pairs) - 1:
            if pairs[i][0] == pairs[i + 1][0] - 1 and pairs[i][1] == pairs[i + 1][1] + 1):
                filter_lst += pairs[i]
        if pairs[i][0] == pairs[i][1] - 1:
            filter_lst += pairs[i]
    return filter_lst
    
def filter_para(word):
    pairs = check_pairs(word)
    filtering = filter_pairs(pairs)
    result = [word[i] for i in range(len(word) if i not in filtering]
    return ''.join(result)
    
print("Welcome to filter useless parentheses")
print("Input a word with parentheses")
print("Output will be useless ones removed")
print("\n~*~--------~*~\n")

para_true = True

while para_true:
    filter_str = raw_input()
    if filter_str.lower() == 'q':
        break
    print(filter_para(filter_str))

raw_input("Press enter to exit.")