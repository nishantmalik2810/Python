#You are given a list arr that contains integers.
#You need to return average of the non negative integers.
n = int(input("Enter the number of element : "))
lst = []
lst1 = []
sum = 0
for i in range(0,n):
    x = int(input(f"Enter element {i+1} : "))
    lst.append(x)
    if x>=0:
        lst1.append(x)
y = len(lst1)
for j in range(0,y):
    sum += lst1[j]
avg = sum/y
print("Complete list : ",lst)
print("List of non-negative integers : ",lst1)
print("Average of non-negative numbers : ",avg)