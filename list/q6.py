#You are given a number k and a list arr that contains integers.
#You need to return list of numbers that are less than k.
n = int(input("Enter the number of element of the list : "))
k = int(input("Enter the value of k : "))
lst = []
lst1 = []
for i in range(1,n+1):
    x = int(input(f"Enter the element {i} : "))
    lst.append(x)
    if(k>x):
        lst1.append(x)
print("Complete list : ",lst)
print(f"List less than {k} is {lst1}")
    
    