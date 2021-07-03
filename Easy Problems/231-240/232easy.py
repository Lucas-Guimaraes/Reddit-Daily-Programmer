#https://www.reddit.com/r/dailyprogrammer/comments/3kx6oh/20150914_challenge_232_easy_palindromes/

#palindrome.txt is a supplementary file to this

#Imports file, sets up as string to use for function
file = open('palindrome.txt', 'r')
lst = []
for line in file.readlines():
    new = line.replace("\n", "")
    new = new.lower()
    lst.append(new)

palin_str = "".join(lst)
remove_lst = []
for i in set(palin_str):
    if i.isalpha():
        continue
    else:
        remove_lst.append(i)

for i in remove_lst:
    palin_str = palin_str.replace(i, '')

#Checks if it is a palindrome
def check(palindrome):
    if palindrome == palindrome[::-1]:
        return "Palindrome"
    else:
        return "Not a palindrome"

print(check(palin_str))
#exit code
raw_input()