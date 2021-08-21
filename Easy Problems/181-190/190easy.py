# https://www.reddit.com/r/dailyprogrammer/comments/2nauiv/20141124_challenge_190_easy_webscraping_sentiments/

import urllib
from sys import argv

url = "https://www.youtube.com/watch?v=9-CHahTFBSM"
page = urllib.urlopen(url)
html = str(page.read())

happy = ["control", "love", "loved", "like", "awesome", "amazing", "good", "great", "excellent"]
sad = ["hate", "hated", "dislike", "disliked", "awful", "terrible", "bad", "painful", "worst"]
happy_count = 0
sad_count = 0
sample_size = 0

for i in happy:
    happy_count += html.count(i)
for i in sad:
    sad_count += html.count(i)

tone = ""
if happy_count > sad_count:
    tone = "HAPPY"
elif sad_count > happy_count:
    tone = "SAD"
else:
    tone = "NEUTRAL"

print(tone)

raw_input("\nPress enter to exit.")