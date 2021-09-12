#https://www.reddit.com/r/dailyprogrammer/comments/5prdgb/20170123_challenge_300_easy_lets_make_some_noise/

#https://docs.python.org/3/library/winsound.html

import winsound
import random
import time

def solfege():
    frequencies = [262, 294, 330, 349, 392, 440, 494, 523]
    duration = 500
    pause = 0.1
    for e in frequencies:
        winsound.Beep(e, duration)
        time.sleep(pause)

def random_freq():
    lst = []
    for i in range(7):
     lst.append(random.randint(37, 32767))
    duration = 500
    pause = 0.1
    for a in lst:
        winsound.Beep(a, duration)
        time.sleep(pause)

if __name__ == '__main__':
    #random_freq()
    solfege()