# https://www.reddit.com/r/dailyprogrammer/comments/x538d/7252012_challenge_81_easy_numerical_calculus_i/

EPSILON = 0.0001

import string

def derivative(y, xmin=None, xmax=None, x=None):
    if xmin is None and xmax is None and x is None:
        print("That didn't work")
        
    if x is None:
        xmin = float(xmin)
        xmax = float(xmax)
        x = []
        xc = xmin
        while xc-xmax < -EPSILON:
            x.append(xc)
            xc += (xmax-xmin)/(len(y)-1)
        x.append(xmax)
    
    result = len(x)*[0]
    for i in range(len(x)-1):
        result[i] = (y[i+1] - y[i]) / (x[i+1] - x[i])
    result[len(x)-1] = result[len(x)-2]
    return result
    
print("Welcome to Derivative!")
print("This function prints out a Derivative of a number.")
print("That is all.")
print("\n~*~----------------~*~\n")
print(derivative(xmin=-1,xmax=1,y=[-1.0,-.5,0,.5,1.0]))
print(derivative(xmin=-10,xmax=10,y=[-1.0,-.5,0,.5,1.0]))
print(derivative(x=[0,2,3,4,5,6,7],y=[-1.0,-.5,0,.5,1.0,1.5,2.0]))
print("\n~*~----------------~*~\n")
raw_input("Press enter to exit.")