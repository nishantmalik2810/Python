'''
Given an integer n.
Write a program to print the inverted "Right angle triangle" wall. 
The length of the perpendicular and base is n.
'''
n = int(input("Enter the base and perpendicular of the triangle : "))
print("Inverted Triangle :-- ")
i=n
while i>=1:
    for j in range(1,i+1):
        print("*", end = "")
    i-=1
    print()
