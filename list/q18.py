'''

Given an array arr[]. Find the majority element in the array.
If no majority element exists, return -1.

Note: A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.

'''

n = int(input("Enter the number of element : "))
lst = []
for i in range(0,n):
    x = int(input(f"Enter element {i+1} of the list : "))
    lst.append(x)
print("COMPLETE LIST : ",lst)
c = 0
for i in lst:
    count = 0
    for j in lst:
        if i == j:
            count+=1
    if count>len(lst)/2:
        print(f"{i} is the majority element")
        c+=1
        break
if c==0:
    print("-1")