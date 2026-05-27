#Given a number n , subtract one from it using bitwise operations.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Perform bitwise subtraction using Two's Complement method
while b:
    borrow = (~a) & b  # Find borrow bits
    a = a ^ b  # Subtract without carrying
    b = borrow << 1  # Shift borrow left
print("Subtraction result:", a)