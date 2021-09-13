#https://www.reddit.com/r/dailyprogrammer/comments/4ad23z/20160314_challenge_258_easy_irc_making_a/

def irc_format(address, nickname, username, realname):
    server = address.split(':')
    print("connected [" + server[0] + server[1] + "]")
    print("NICK " + nickname)
    print("USER " + username + " 0 * :" + realname)

irc_format('chat.freenode.net:6667',
    'Hello',
    'World',
    'New')