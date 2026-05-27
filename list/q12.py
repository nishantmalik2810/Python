'''
Given an array arr[] of positive integers. Reverse every sub-array group of size k.
Note: If at any instance, k is greater or equal to the array size,
then reverse the entire array.
You shouldn't return any array, modify the given array in place.

'''

n = int(input("Enter the number of element : "))
k = int(input("Enter the value of K = "))
lst = []
for i in range(0,n):
    x = int(input(f"Enter element {i+1} of the list : "))
    lst.append(x)
print("COMPLETE LIST : ",lst)
if k >= n:
    lst.reverse()
else:
    i = 0
    while i < n:
        end = i + k
        if end <= n:
            sublist = lst[i:end]
            sublist.reverse()
            lst[i:end] = sublist
        else:
            sublist = lst[i:]
            sublist.reverse()
            lst[i:] = sublist
        i += k
print("Modified Array:", lst)