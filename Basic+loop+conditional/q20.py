'''
You are given a number n. The number n can be negative or positive.
If n is negative, print numbers from n to 0 by adding 1 to n in the neg function.
If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.
Note:- You don't have to return anything, you just have to print the array.
'''

n = int(input("Enter the number : "))
if(n<0):
    i = n
    while i<=0:
        print(i)
        i+=1
if(n>0):
    j=n-1
    while j>=0:
        print(j)
        j-=1