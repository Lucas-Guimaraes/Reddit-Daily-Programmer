#https://www.reddit.com/r/dailyprogrammer/comments/5wnbsi/20170228_challenge_304_easy_little_accountant/

#Organizing data
chart = open('304easychart.txt', 'r')
journal = open('304easyjournal.txt', 'r')
chart_lst = []
journal_lst = []
dict_format = {'JAN-16': 0,
               'FEB-16': 1,
               'MAR-16': 2,
               'APR-16': 3,
               'MAY-16': 4,
               'JUN-16': 5,
               'JUL-16': 6}

for c in chart:
    c = c.replace('\n', '')
    c = c.split(';')
    c = (int(c[0]), c[1])
    chart_lst.append(c)

for j in journal:
    j = j.replace('\n', '')
    j = j.split(';')
    j = [int(j[0]), dict_format[j[1]], int(j[2]), int(j[3])]
    journal_lst.append(j)

valid_entries = [i[0] for i in chart_lst]
etc = [i[1] for i in chart_lst]
chart_dict = { k:v for (k,v) in zip(valid_entries, etc)}




def account_journal(start, end, start_date, end_date):
    #Checks any infinities plus handles dates
    if start == '*':
        start = 1
    if end == '*':
        end = 9100
    if start_date == '*':
        start_date = 0
    else:
        start_date = dict_format[start_date]
    if end_date == '*':
        end_date = 6
    else:
        end_date = dict_format[end_date]

    #Outer loop checks start and end, inner loop checks all the journal entries with that valid start date
    #Basically, outer is start/end account. Inner is start/end date.
    ledger_lst = []
    valid_dates = range(start_date, end_date+1)
    for i in range(start, end):
        if i in valid_entries:
            credit = 0
            debit = 0
            balance = 0
            for j in journal_lst:
                if j[0] == i and j[1] in valid_dates:
                    debit += j[2]
                    credit += j[3]
            balance = debit - credit

            if balance != 0:
                ledger_lst.append([i, chart_dict[i], debit, credit, balance])

    #Prints the ledger list followed by the total
    total_debit = 0
    total_credit = 0
    total_balance = 0
    for l in ledger_lst:
        total_credit += l[2]
        total_debit += l[3]
        total_balance += l[4]
        print('{} | {} | {} | {} | {}'.format(str(l[0]), str(l[1]), str(l[2]), str(l[3]), str(l[4])))
    print('TOTAL |   | {} | {} | {}'.format(total_debit, total_credit, total_balance))

#Test Case
account_journal('*', 2001, '*', 'FEB-16')