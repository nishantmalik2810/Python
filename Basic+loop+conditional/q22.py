'''
Given two integers n and m. The problem is to find the number closest to n and divisible by m. 
If there is more than one such number,
then output the one having the maximum absolute value.
'''
n = int(input("Enter n :- "))
m = int(input("Enter m :- "))
for i in range(1 , n+1):
    if(i%m==0):
        q=i
print(q)