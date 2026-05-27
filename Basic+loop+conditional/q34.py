'''
Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number.
Given a number N, the task is to check if it is a Strong Number or not. Print 1 if the Number is Strong, else Print 0.
'''
n = int(input("Enter the number : "))
b=n
r = 0
sum = 0
while b>0:
    r = b%10
    fact = 1
    for i in range(1,r+1):
        fact=fact*i
    sum = sum + fact
    b=b//10
if(sum==n):
    print("Strong Number so 1")
else:
    print("Not a strong number so 0")