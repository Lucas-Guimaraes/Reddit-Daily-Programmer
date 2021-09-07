#https://www.reddit.com/r/dailyprogrammer/comments/31ls3h/20150406_challenge_209_easy_the_button_can_be/

def the_button(data):
    presses = {}
    for i in data:
        time = i[1]
        presses[time] = i[0]

    sortedtimes = [0]
    sortedtimes.extend(sorted(presses))
    for i, time in enumerate(sortedtimes[1:]):
        print('{}: {}'.format(presses[time], int(60 - time + sortedtimes[i])))

the_button([('Coder_d00d', 3.14), ('Cosmologicon', 22.15), ('Elite6809', 17.25), ('jnazario', 33.81), ('nint22', 10.13), ('rya11111', 36.29), ('professorlamp', 31.60), ('XenophonOfAthens', 28.74)])
