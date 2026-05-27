'''
Given an array arr[].
Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer.
Do the mentioned change in the array in place.

Note: Consider the array as circular.

'''

n = int(input("Enter the number of element : "))
d = int(input("Enter the value of d = "))
lst = []
for i in range(0,n):
    x = int(input(f"Enter element {i+1} of the list : "))
    lst.append(x)
print("COMPLETE LIST : ",lst)
#using slicing
d=d%n
lst[:] = lst[d:] + lst[:d]
print("LIST AFTER ROTATION : ",lst)
        