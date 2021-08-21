import string

def ver_lst(lst):
    #Sorts first, then second
    lst.sort(lambda x,y: (
   cmp(string.split(x)[-1], string.split(y)[-1]) or  # Sort by last name...
   cmp(x, y)))                                       # # ...then by first name
    skip = True
    for x in range(len(lst)):
        cur = lst[x]
        #Checks extra version
        if cur.find('-') > 0 and len(lst) != x and skip:
            cur = cur[cur.find('-')]
            if cur in lst[x+1]:
                lst[x], lst[x+1] = lst[x+1], lst[x]
        #Makes sure switcharoo doesn't happen
        if skip == False:
            skip = True
    for x in lst:
        print x
    return

ver_lst(['2.0.11-alpha', '0.1.7+amd64', '0.10.7+20141005', '2.0.12+i386', '1.2.34', '2.0.11+i386', '20.1.1+i386'])