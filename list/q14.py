'''
You are given a positive integer n, you need to add all the digits of n and create a new number.
Perform this operation until the resultant number has only one digit in it.
Return the final number obtained after performing the given operation.
'''
n = int(input("Enter the number: "))

while n >= 10:
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    n = sum

print("Final single-digit sum is:", n)