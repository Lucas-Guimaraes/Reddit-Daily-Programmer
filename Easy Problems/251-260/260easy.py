# https://www.reddit.com/r/dailyprogrammer/comments/4cb7eh/20160328_challenge_260_easy_garage_door_opener/

#initializes class
class GarageDoor:
    def __init__(self):
        self.state = "CLOSED"

    def click(self, command):
        #if the button is clicked, checks if opening or closing
        if command == "button_clicked":
            if self.state == "OPEN":
                self.state = "CLOSING"
            else:
                self.state = "OPENING"
        #if cycle is complete, we change to open/closed
        elif command == "cycle_complete":
            if self.state == "OPEN":
                self.state = "OPEN"
            else:
                self.state = "CLOSED"
        #returns result
        return self.state

#makes object, uses commands
door = GarageDoor()

print door.click("button_clicked")
print door.click("cycle_complete")
print door.click("button_clicked")
print door.click("button_clicked")
print door.click("button_clicked")
print door.click("button_clicked")
print door.click("button_clicked")
print door.click("cycle_complete")

raw_input("\nPress enter to exit.")