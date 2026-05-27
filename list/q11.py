'''
You are given an array arr[] of non-negative integers.
Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements.
The operation must be performed in place, meaning you should not use extra space for another array.
'''

n = int(input("Enter the number of element : "))
lst = []
for i in range(0,n):
    x = int(input(f"Enter element {i+1} of the list : "))
    lst.append(x)
print("COMPLETE LIST : ",lst)

# using enumerate
count =0
for idx, val in enumerate(lst):
    if val != 0:
        lst[count] = val
        count += 1

# Fill the remaining part with 0s
for i in range(count, n):
    lst[i] = 0

print("MODIFIED LIST:", lst)
       