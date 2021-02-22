# https://www.reddit.com/r/dailyprogrammer/comments/s6bas/4122012_challenge_39_easy/
def fizzbuzz(n):
    
    for i in range(n+1):
    
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    return
print("Welcome to FizzBuzz!")
print("You will insert a number.")
print("After you do so, it will print every number before and the current number")
print("Every number divisible by 3, that number will print 'Fizz' instead")
print("Every number divisible by 5, that number will print 'Buzz' instead")
print("If a number is printable by both 3 and 5, it will print 'FizzBuzz'")

print("\n~*~--------~*~\n")
fizzbuzz(int(raw_input("Please put in your number: "))) 


#fizzbuzz(69)
raw_input("\nPress enter to exit")