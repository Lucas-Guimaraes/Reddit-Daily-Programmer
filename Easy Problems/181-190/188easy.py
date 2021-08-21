# https://www.reddit.com/r/dailyprogrammer/comments/2lvgz6/20141110_challenge_188_easy_yyyymmdd/
# '188easydates.txt' is a supplementary file to this challenge.

dates = []
f = open("188easydates.txt", "r")

#prepares our date list
for line in f.readlines():
    dates.append(line.replace("\n", ""))
    
months = {'Jan': '01',
'Feb': '02',
'Mar': '03',
'Apr': '04',
'May': '05',
'Jun': '06',
'Jul': '07',
'Aug': '08',
'Sep': '09',
'Oct': '10',
'Nov': '11',
'Dec': '12'
}

def date_cleanup(lst):
    new_lst = []
    for i in lst:
        temp_str = ''

        # yyyy-mm-dd to yyyy-mm-dd
        if i[4] == '-' and i[7] == '-':
            new_lst.append(i)

        # mm/dd/yy to yyyy-mm-dd
        elif i[2] == '/' and i[5] == '/':
            if int(i[6:] >= 50):
                temp_str += str(19)
            else:
                temp_str += str(20)

            temp_str += i[6:] + '-' + i[0:2] + '-' + i[3:5]
            new_lst.append(temp_str)

        # mm#yy#dd to yyyy-mm-dd
        elif i[2] == '#' and i[5] == '#':
            if int(i[3:5] >= 50):
                temp_str += str(19)
            else:
                temp_str += str(20)

            temp_str += i[3:5] + '-' + i[0:2] + '-' + i[6:]
            new_lst.append(temp_str)

        # dd*mm*yyyy to yyyy-mm-dd
        elif i[2] == '*' and i[5] == '*':
            temp_str += i[6:] + '-' + i[3:5] + '-' + i[0:2]
            new_lst.append(temp_str)

        # (month word) dd, yy to yyyy-mm-dd
        elif i[0:3].isalpha() and len(i) == 10:
            if int(i[9:] >= 50):
                temp_str += str(19) + i[8:]
            else:
                temp_str += str(20) + i[8:]
            temp_str += '-' + months[i[0:3]] + '-' + i[4:6]
            new_lst.append(temp_str)

        # (month word) dd, yyyy to yyyy-mm-dd
        elif i[0:3].isalpha():
            temp_str += i[8:] + '-' + months[i[0:3]] + '-' + i[4:6]

            new_lst.append(temp_str)
    for n in new_lst:
        print(n)
        
date_cleanup(dates)
raw_input()