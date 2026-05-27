'''
You are given a 3-digit number n, Find whether it is an Armstrong number or not.

An Armstrong number of three digits is a number such that 
the sum of the cubes of its digits is equal to the number itself. 
371 is an Armstrong number since 33 + 73 + 13 = 371. 
'''

n = int(input("Enter the 3-digit number : "))
c = n
a=0
b=0
while c>0:
    a = c%10
    c = c//10
    b = a**3 + b
if(b==n):
    print("Armstrong")
else:
    print("Not Armstrong")
    