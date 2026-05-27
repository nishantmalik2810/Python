'''
You are given an integer n, return the fibonacci series till the nth(0-based indexing) term.
'''
def fib(n):
    a = 0
    b = 1
    if(n==0):
        print(a)
    elif(n>=1):
        print("0th indexed based fibonacci :-- ")
        print(a,end = " ")
        print(b,end = " ")
        i = 2
        while i<=n:
            a,b=b,a+b
            i+=1
            print(b,end = " " if i<=n else "")
n = int(input("Enter the index number : "))
fib(n)