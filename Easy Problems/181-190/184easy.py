#https://www.reddit.com/r/dailyprogrammer/comments/2j5929/10132014_challenge_184_easy_smart_stack_list/

class SmartList:
    def __init__(self):
        self.lst = []

    def push(self, n):
        self.lst.append(n)

    def pop(self):
        if len(self.lst) >= 1:
            self.lst.pop()
        else:
            print("No valid items to pop!")

    def size(self):
        print(len(self.lst))

    def greater(self, n):
        remove_lst = []
        for i in self.lst:
            if i > n:
                remove_lst.append(i)
        for i in remove_lst:
            self.lst.remove(i)

    def displaystack(self):
        print(self.lst)

    def displayordered(self):
        print(sorted(self.lst))


#Input
print("Welcome to Smart Stack List!")
print("This program has numerous methods")
print("Push, Pop, Size, Greater, DisplayStack, and DisplayOrdered")
print("Greater and Push will require a number; the rest will not")
print("Example Input:")
print("Push 14")
print("Display Stack")
print("Example Output:")
print("14")

print("\n~*~----------------~*~\n")

#Run code, instantiate class
smart_list = SmartList()
program = True

while program:
    m = raw_input("m: ").lower()
    if m == "q":
        break

    #Cleans up input
    m = m.split()
    #Valid checkers
    double_valid = ['push', 'greater']
    valid = ["displaystack", "displayordered", "pop", "size"]

    #Solves for two inputs
    if len(m) >= 2:
        if m[0] in double_valid and m[1].isdigit():
            command = "smart_list." + m[0] + "(int({}))".format(m[1])
            eval(command)

    #Solves for one input
    m = ''.join(m)
    if m in valid:
        command = "smart_list." + m + "()"
        eval(command)

raw_input("Press enter to exit.")

#Test cases

#smart_list = SmartList()
#smart_list.push(14)
#smart_list.push(24)
#smart_list.push(8)
#smart_list.push(18)
#smart_list.displaystack()
#smart_list.displayordered()
#smart_list.pop()
#smart_list.displayordered()
#smart_list.size()
#smart_list.push(24)
#smart_list.greater(23)
#smart_list.displayordered()