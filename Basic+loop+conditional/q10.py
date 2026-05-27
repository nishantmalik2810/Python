#Given an integer n,  write a program to print the square wall of size n using nested loops.
# Try not to use String multiplication.
n = int(input("Enter the side of square : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end = "")
    print()
