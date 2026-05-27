#Given a positive integer x, the task is to print the numbers 
# from 1 to x in the order as 1^2, 3^2, 4^2, 5^2, ... (in increasing order).

x = int(input("Enter x : "))
i = 1
while i<=x:
    print(i**2,end = " "if i<x else "")
    i+=1

