'''
Given a number n, find the value of n raised to the power of its own reverse.
Constraints:
1 <= n <= 10
'''

def power(n):
    i = n
    if i<10:
        print(i**i)
    elif i==10:
        print(i)
n = int(input("Enter the number between 1 to 10 : "))
power(n)