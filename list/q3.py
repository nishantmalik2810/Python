#You are given a list that contains integers. 
#You need to return the sum of the list.

n = int(input("Enter the number of elements of the string : "))
list = []
sum = 0
for i in range(0 , n):
    x = int(input(f"Enter the element {i} of the string : "))
    list.append(x)
    sum += list[i]
print("Sum of all the elements of the list is ",sum)
