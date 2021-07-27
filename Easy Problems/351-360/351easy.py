#https://www.reddit.com/r/dailyprogrammer/comments/7x81yg/20180213_challenge_351_easy_cricket_scoring/

#Input cricket card; output cricket score
def cricket(s):
    #If 'w' or 'b', add one to extra
    extra = [i for i in s if i in ('wb')]

    #Replace 'w' with '', and '.' with '0'
    score = s.replace('w', '').replace('.', '0')
    res, players = [], [1, 2]

    for ball, i in enumerate(score, 1):

        #move players to the next player
        if i == 'W':
            res.append((players[0], 0))

            #Code to add player 1 just in-case
            if len(res) == 1:
                res.append((players[1], 0))
            players = [max(players) + 1, players[1]]

        #move to the last player on the current list
        elif i == 'b':
            res.append((players[0], 0))
            players = players[::-1]

        #change to different player, add points
        elif int(i) % 2 == 0:
            res.append((players[0], int(i)))
            if ball % 6 == 0:
                players = players[::-1]

        #add points, change player
        else:
            res.append((players[0], int(i)))
            players = players[::-1]

    #Makes dictionary out of tuples
    d = {k:v for k, v in res}
    #Groups the points with player
    grouped = [(x, sum(v for k, v in res if k == x)) for x in d.keys()]

    #Prints out scorecard
    for i in grouped:
        print('P' + str(i[0]) + ": {}".format(i[1]))
    print('Extra: {}'.format(len(extra)))

#Checks if valid cricket score:
def valid_cricket(s):
    for i in s:
        if i not in '0123456789wWb.':
            return False
    return True

#Intro
print("Welcome to Cricket Scoring")
print("This will take a score input and output it as a cricket scorecard")
print("\n~*~----------------~*~\n")

#Continue Code
playing_cricket = True
while playing_cricket:
    scorecard = raw_input().replace(' ', '')
    if scorecard.lower() == 'q':
        break
    if valid_cricket(scorecard):
        cricket(scorecard)

raw_input("Press Enter to exit.")

#Test Cases
#cricket('1.2wW6.2b34')
#cricket('WWWWWWWWWW')
#cricket('1..24.w6')