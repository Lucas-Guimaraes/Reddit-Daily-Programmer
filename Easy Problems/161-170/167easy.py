#https://www.reddit.com/r/dailyprogrammer/comments/289png/6162014_challenge_167_easy_html_markup_generator/

#167easy.html is a supplementary file
#167easy.css is also a supplementary file

import webbrowser

file = open('167easy.html', 'w')

code = """
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="167easy.css">
        <title></title>
    </head>

    <body>
        <p> %s </p>
    </body>
</html>
""" % raw_input("Enter your paragraph: ")
file.write(code)
webbrowser.open('167easy.html')

file.close()


