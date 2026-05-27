'''
Print numbers from 1 to n without the help of loops.
You only need to complete the function printNos() 
that takes n as a parameter and prints the number from 1 to n recursively.
'''
def count(n):
    if (n==0):
        return
    count(n-1)
    print(n,end = " ")
n = int(input("Enter number : "))
count(n)