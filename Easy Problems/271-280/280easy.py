#https://www.reddit.com/r/dailyprogrammer/comments/4z04vj/20160822_challenge_280_easy_0_to_100_real_quick/

#Hands
hand = {'00000': 0,
              '01000': 1,
              '01100': 2,
              '01110': 3,
              '01111': 4,
              '10000': 5,
              '11000': 6,
              '11100': 7,
              '11110': 8,
              '11111': 9,}

def hand_count(n):
    right_hand = 0
    left_hand = 0

    #Checks if right hand is valid
    if n[5:] in hand:
        right_hand = hand[n[5:]]
    else:
        return "Invalid"
    n = n[0:5]

    #Checksi f left hand is valid
    if n[::-1] in hand:
        left_hand = hand[n[::-1]] * 10
    else:
        return "Invalid"

    return left_hand + right_hand

print(hand_count('0011101110'))