'''
Here two integers a and b are given.
The given input and its values are passed as arguments to the function argumentFunction.
The argumentFunction is responsible to return (a+b). You need to write this function.
'''
def function(a,b):
    return a+b

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
x = function(a,b)
print("Value of a+b : ",x)