'''

You are given two arrays a[] and b[], return the Union of both the arrays in any order.

The Union of two arrays is a collection of all distinct elements present in either of the arrays.
If an element appears more than once in one or both arrays, it should be included only once in the result.

Note: Elements of a[] and b[] are not necessarily distinct.
Note that, You can return the Union in any order but the driver code will print the result in sorted order only.

'''

n1 = int(input("Enter the number of element of list A : "))
n2 = int(input("Enter the number of element of list B : "))
lst = []
lst1 = []
for i in range(0,n1):
    x = int(input(f"Enter element {i+1} of the list A : "))
    lst.append(x)
for i in range(0,n2):
    x = int(input(f"Enter element {i+1} of the list B : "))
    lst1.append(x)
print("COMPLETE LIST A : ",lst)
print("COMPLETE LIST B : ",lst1)
union = list(set(lst + lst1))
union.sort()
print("UNION OF BOTH LISTS:", union)