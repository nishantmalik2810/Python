'''
Given a number n, check if a number is perfect or not.
A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number. 
'''
n = int(input("Enter a number : "))
b = 0
for i in range(1,n):
    if(n%i==0):
        b+=i
if(b==n):
    print("Perfect number")
else:
    print("Not a perfect number")