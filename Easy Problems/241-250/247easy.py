# https://www.reddit.com/r/dailyprogrammer/comments/3yiy2d/20151228_challenge_247_easy_secret_santa/

import random

file = open('secretsanta.txt', 'r')
count = 1
secret_d = {}

for line in file.readlines():
    new = line.replace("\n", "")
    new_list = []
    new_list = new.split()
    if len(new_list) > 0:
        secret_d[count] = new_list
    else:
        secret_d[count] = new
    count += 1


def secret_santa(d):
    giver, receiver = list(d.values()), list(d.values())
    gifts = []

    while len(giver) > 0 and len(receiver) > 0:
        a = random.choice(giver)
        b = random.choice(receiver)
        store_a = ''
        store_b = ''
        old_a = ''
        old_b = ''
        store_a_2 = []
        store_b_2 = []
        if a == b:
            continue
        if len(a) > 1:
            store_a = giver.index(a)
            old_a = a
            a = random.choice(a)
        if len(b) > 1:
            store_b = receiver.index(b)
            old_b = b
            b = random.choice(b)

        a_add, b_add = str(a), str(b)
        a_add, b_add = a_add.replace('[', '').replace(']', '').replace("'", ''), b_add.replace('[', '').replace(']', '').replace("'", '')
        new_gift = '{} -> {}'.format(a_add, b_add)
        gifts.append(new_gift)

        mememagic = ''
        if store_a == '':
            giver.remove(a)
        else:
            for i in old_a:
                if i != a:
                    store_a_2.append(i)

            giver[store_a] = store_a_2

        if store_b == '':
            receiver.remove(b)
        else:
            for i in old_b:
                if i != b:
                    store_b_2.append(i)
                    receiver[store_b] = store_b_2

    for i in gifts:
        print(i)


secret_santa(secret_d)
raw_input()