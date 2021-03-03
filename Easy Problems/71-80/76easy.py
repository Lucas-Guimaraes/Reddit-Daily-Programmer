#https://www.reddit.com/r/dailyprogrammer/comments/wjzly/7132012_challenge_76_easy_title_case/

#sen = sentence
#exc = exceptions
def titlecase(sen, exc):
    titled = []
    sen = sen.split()
    for word in sen:
        temp_word = word.lower()
        if temp_word in exc:
            titled.append(temp_word)
            continue
        temp_word = temp_word.title()
        titled.append(temp_word)
    titled = " ".join(titled)
    titled = titled[0].title() + titled[1:]
    return titled

def quit_check(i):
    if i == 'q':
        answer = raw_input("Are you sure? Type 'y' or 'yes' to confirm. This is not case sensitive: ").lower()
        if answer == 'yes' or answer == 'y':
            print("Goodbye.")
            return True
    return False
    
print("Welcome to title case!")
print("This takes two inputs: Exceptions (a list) and your sentence")
print("Afterwards, it will titlecase everything except the exceptions")

print("\n Example Input:")
print("Exceptions: jumps, the, over")
print("Sentence: The quick brown fox jumps over the lazy dog")

print("\n Example Output:")
print("The Quick Brown Fox jumps over the Lazy Dog")

print("\n~*~----------------~*~\n")

sen = True
quitting = False
while sen:
    first_put = True
    while first_put:
        exc = raw_input("Please input your list. 'q' to quit: ").lower().replace(',', '')
        if quit_check(exc):
            quitting = True
        exc = exc.split()
        first_put = False
    if quitting:
        break
    
    second_put = True
    while second_put:
        sentence = raw_input("Now for your sentence: ")
        if quit_check(sentence):
            quitting = True
        second_put = False
    if quitting:
        break
    
    print(titlecase(sentence, exc))
    
    

#exceptions = ['are', 'is', 'in', 'your', 'my']
#print(titlecase('THE vitamins ARE IN my fresh CALIFORNIA raisins', exceptions))

raw_input()
