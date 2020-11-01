#https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
#This involved making a calculator

first_number = 0
second_number = 0
ending_number = 0
order_list = []

#checks if digit
def check_digit(x):
    while True:
        store_number = raw_input(x)
        try:        
            store_number = int(store_number)
            return store_number
            break
        except ValueError:
            store_number = str(store_number)
            print(store_number + " is not a valid number! Try again.")
#math functions
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
    
#order
def order():    
    while True:
        print "1. " + str(first_number) + " goes first" 
        print "2. " + str(second_number) + " goes second"
        order_select = raw_input("Which order would you like to subtract or divide these numbers in?: ")
        if order_select == "1":
            order_list.append(first_number)
            order_list.append(second_number)
            break
        elif order_select == "2":
            order_list.append(second_number)
            order_list.append(first_number)
            break
        else:
            print("That's not '1' or '2'")

#this carries out the operation            
def operation(x, y):
    while True:
        print "Please select an operation."
        print "1. Add"
        print "2. Subtract"
        print "3. Multiply"
        print "4. Divide"
        operation_selection = raw_input("Please put in the number for whichever operation you want: ")
        if operation_selection == "1":
            operation_selection = add(first_number, second_number)
            print("Your result is: " + str(operation_selection))
            break
        elif operation_selection == "2":
            order()
            operation_selection =  subtract(order_list[0], order_list[1])
            print("Your result is: " + str(operation_selection))
            break
        elif operation_selection == "3":
            operation_selection = multiply(first_number, second_number)
            print("Your result is: " + str(operation_selection))
            break
        elif operation_selection == "4":
            order()
            operation_selection =  subtract(order_list[0], order_list[1])
            print("Your result is: " + str(operation_selection))
            break
        else:
            print("That's not '1', '2', '3', or '4'!")



first_number = check_digit("Please put in your first number: ")
print("Your first number is " + str(first_number))
second_number = check_digit("Please put in your second number: ")
print("Your second number is " + str(second_number))
operation(first_number, second_number)
raw_input()
