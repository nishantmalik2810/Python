'''
Given an array of positive integers arr[],
return the second largest element from the array.
If the second largest element doesn't exist then return -1.
Note: The second largest element should not be equal to the largest element.
'''
n = int(input("Enter the number of element : "))
lst = []
for i in range(0,n):
    x = int(input(f"Enter element {i+1} of the list : "))
    lst.append(x)
print("COMPLETE LIST : ",lst)
lst.sort(reverse=True)
max_val = lst[0]
second_largest = -1
for num in lst:
    if num < max_val:
        second_largest = num
        break

print("Second Largest =", second_largest)
