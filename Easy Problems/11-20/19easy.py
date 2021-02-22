# https://www.reddit.com/r/dailyprogrammer/comments/qlwrc/372012_challenge_19_easy/

def remove_sherlock(text):
    holmes = open(text, "r")
    holmes_read = holmes.read()
    chapters = ["I. A Scandal in Bohemia"
            "II. The Red-headed League",
            "III. A Case of Identity",
            "IV. The Boscombe Valley Mystery",
            "V. The Five Orange Pips",
            "VI. The Man with the Twisted Lip",
            "IX. The Adventure of the Engineer's Thumb",
            "X. The Adventure of the Noble Bachelor",
            "XI. The Adventure of the Beryl Coronet",
            "XII. The Adventure of the Copper Beeches"]
    for chapter in chapters:
        holmes_read.replace(chapter, "")
    caps_venture = 'adventure'.upper()
    holmes_read.replace(caps_venture, "")
    holmes_read = holmes_read.split('\n')
    holmes_read = holmes_read[61:12630]
    
    holmes_read = "".join(holmes_read)
    
    chars = 0
    for line in holmes_read:
        
        for c in line:
            
            if c.isalnum():
                chars += 1
    return chars
    
sherlock = '19easysherlock.txt'
print(remove_sherlock(sherlock))
raw_input()

