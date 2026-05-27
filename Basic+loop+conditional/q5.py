#Given two numbers a and b, you need to swap their values so a holds the value of b and b holds the value of a.

a = float(input("Enter the value of 'a' : "))
b = float(input("Enter the value of 'b' : "))

a,b=b,a

print("After swapping :- ")
print("a = ",a)
print("b = ",b)
