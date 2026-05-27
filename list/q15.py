'''
Given an unsorted array arr containing both positive and negative numbers.
Your task is to rearrange the array and convert it into an array of alternate
positive and negative numbers without changing the relative order.

Note:
- Resulting array should start with a positive integer (0 will also be considered as a positive integer).
- If any of the positive or negative integers are exhausted,
    then add the remaining integers in the answer as it is by maintaining the relative order.
- The array may or may not have the equal number of positive and negative integers.

'''
n = int(input("Enter the number of element : "))
lst = []
for i in range(0,n):
    x = int(input(f"Enter element {i+1} of the list : "))
    lst.append(x)
print("COMPLETE LIST : ",lst)
positive = []
negative = []
for i in range(n):
    if lst[i]>=0:
        positive.append(lst[i])
    else:
        negative.append(lst[i])
i=0
j=0
k=0
res =[]
while i <len(positive) and j<len(negative):
    if k%2==0:
        res.append(positive[i])
        i+=1
    else:
        res.append(negative[j])
        j+=1
    k+=1
while i < len(positive):
    res.append(positive[i])
    i += 1
while j < len(negative):
    res.append(negative[j])
    j += 1
print("REARRANGED LIST : ",res)