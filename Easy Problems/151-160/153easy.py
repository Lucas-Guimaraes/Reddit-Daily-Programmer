# https://www.reddit.com/r/dailyprogrammer/comments/20l2it/17042014_challenge_153_easy_pascals_pyramid/


def pascal_pyramid(n):
    A = [1]
    lst = []
    for i in range(n):
        B=[sum(A[j:j+2]) for j in range(i)]
        B[:0]=[1]
        B[i+1:]=[1]
        str_a = "".join(str(A))
        str_a = str_a.replace("[", "").replace("]", "").replace(",", "")
        lst.append(A)
        A = B

    #prepares string formatting
    top = len(str(lst[-1]))
    if top % 2 != 0:
        top += 1

    #prints strings
    for i in range(len(lst)):
        cur_line = str(lst[i])
        cur_line = cur_line.replace("[", "").replace("]", "").replace(",", "")
        cur = len(cur_line)
        mid = (top - cur) / 2
        if cur % 2 != 0:
            print((' ' * mid) + cur_line + (' ' * (mid - 1)))
        else:
            print((' ' * mid) + cur_line + (' ' * mid))

pascal_pyramid(10)
raw_input()