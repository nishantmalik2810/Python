'''
Given a number n, find the first digit of the number.
'''
def first_digit(n):
    a = n
    while a>10:
        a = a//10
    return a
n = int(input("Enter the number : "))
x = first_digit(n)
print("First digit of the number is : ",x)
