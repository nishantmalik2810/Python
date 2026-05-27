'''
Given an integer n. Write a program to find the nth Fibonacci number.
F(0)= 0, F(1)=1
The nth Fibonacci number is given by the forumla F(n) = F(n-1) + F(n-2). The first few fibonacci numbers are: 0 1 1 2 3 5. . . . 
'''
n = int(input("Enter the number : "))
a = 0
b = 1
if(n==1):
    print(f"{n} fibonacci number is {a}")
elif(n==2):
    print(f"{n} fibonacci number is {b}")
else:
    i = 3
    while i<=n:
        a,b=b,a+b
        i+=1
    print(f"{n} fibonacci number is {b}")
