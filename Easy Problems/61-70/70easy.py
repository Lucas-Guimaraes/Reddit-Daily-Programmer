#https://www.reddit.com/r/dailyprogrammer/comments/vsv3g/6292012_challenge_70_easy/

#this function takes a file, reads all the letters, lowercases them, and splits them
#the words then have a dictionary
#if the word is not in the dictionary, it gets added with a '1'
#if the word is already in the dictionary, '1' gets added to it
#afterwards, the dictionary is sorted by the biggest numbers first, done via reversing it
#print(and the top * amount [n being done by the user] are chosen)

def common(filename, n):
    content=open('70easyread.txt', 'r').read().lower().split()
    words = {}
    for word in content:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    sorted_words = sorted(words)[::-1]

    return sorted_words[:n]

print(common("70easy.txt", 2))
raw_input("Press enter ti exit")