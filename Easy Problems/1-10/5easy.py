#https://www.reddit.com/r/dailyprogrammer/comments/pnhyn/2122012_challenge_5_easy/

#rstrip strips characters
#login_info = open("easy5supplement.txt", "r")
login_info_lines = [line.rstrip('\n') for line in open("easy5supplement.txt")] #the readlines into a list
correct_username = login_info_lines[0]
correct_password = login_info_lines[1]

while True:
    print("Please enter your username and password to log in")
    username = str(raw_input("Username: "))
    password = str(raw_input("Password: "))
    
    if username == correct_username and password == correct_password:
        print("You have successfully logged in!")
        break
    else:
        print("Please put in the correct username and password.")

raw_input()