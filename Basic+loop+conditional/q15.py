#Given a number N, write a program to check whether given number is Adam Number or not.
#Adam number is a number when reversed, the square of the number 
# and the square of the reversed number should be numbers which are reverse of each other.

n = int(input("Enter the number: "))
reversed_n = int(str(n)[::-1])

square_n = n ** 2
square_reversed_n = reversed_n ** 2
if str(square_n) == str(square_reversed_n)[::-1]:
    print("Adam Number")
else:
    print("Not an Adam Number")