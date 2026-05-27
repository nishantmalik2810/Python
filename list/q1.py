#You are given a list that contains integers.
#You need to print the elements of the list with a space between them.

n = int(input("Enter the number of elements of the string : "))
list = []
for i in range(1,n+1):
    x = input(f"Enter the element {i} of the list : ")
    list.append(x)
for i in range(0,n):
    print(list[i],end =" "if i<n-1 else "")

    
