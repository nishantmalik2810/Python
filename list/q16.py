'''

You are given an array arr of positive integers.
Your task is to find all the leaders in the array. 
An element is considered a leader if it is greater than or equal to all elements to its right.
The rightmost element is always a leader.

'''

n = int(input("Enter the number of element : "))
lst = []
for i in range(0,n):
    x = int(input(f"Enter element {i+1} of the list : "))
    lst.append(x)
print("COMPLETE LIST : ",lst)
leader =[]
for i in range(0,n):
    for j in range(i + 1, n):
        if lst[i] < lst[j]:
            break
    else:
        leader.append(lst[i])
print(leader)