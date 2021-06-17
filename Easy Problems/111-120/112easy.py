# https://www.reddit.com/r/dailyprogrammer/comments/137f7t/11142012_challenge_112_easyget_that_url/

import re, string

def parse_url(url):
    legal_chars = "0-9A-Za-z" + re.escape("-_.~!*'();:@&=+$,/?%#[]")
    check_url = re.match("[{}]+$".format(legal_chars), url)
    #makes sure that there are no invalid characters used in the URL.
    if check_url == None:
        print("The URL you have chosen is invalid")
        return
    print("{} is a valid URL!".format(url))
    
    #tells any actions such-as title, value, etc that have '='
    for key, value in re.findall("(\w+)\=(\w+)", url):

        print("{}: \"{}\"".format(key, value))


#parse_url("http://en.wikipedia.org/w/index.php?title=Main_Page&action=edit")
#parse_url("https://www.reddit.com/r/dailyprogrammer/comments/137f7t/11142012_challenge_112_easyget_that_url/")
#parse_url("https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=rack+mount+samson")

parse = raw_input("Validate a url!:\n\n")
print("\n~*~----------------~*~\n")
parse_url(parse)
print("\n~*~----------------~*~\n")
raw_input("Press enter to exit")