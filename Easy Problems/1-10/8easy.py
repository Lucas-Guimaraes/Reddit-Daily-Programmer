#https://www.reddit.com/r/dailyprogrammer/comments/pserp/2162012_challenge_8_easy/
#am confused by the extra credit?
beer = 99
beerloss = 99
 
while True:

    if beer > 2:
        beerloss -= 1
        print str(beer) + """ bottles of beer on the wall,
""" + str(beer) + """ bottles of beer.
""" + """You take one down, pass it around
""" + str(beerloss) + """ bottles of beer on the wall.
"""
        beer -= 1
    elif beer == 2:
        beerloss -= 1
        print str(beer) + """ bottles of beer on the wall,
""" + str(beer) + """ bottles of beer.
""" + """You take one down, pass it around
""" + str(beerloss) + """ bottle of beer on the wall.
"""
        beer -= 1
    elif beer == 1: 
        print str(beer) + """ bottle of beer on the wall,
""" + str(beer) + """ bottle of beer.
""" + """You take one down, pass it around
No more bottles of beer on the wall.
"""
        beer -= 1
    else:
        print """No more bottles of beer on the wall,
No more bottles of beer,
Go to the store and buy some more,
So we can get 99 more bottles of beer on the wall.
"""
        break
        
raw_input()