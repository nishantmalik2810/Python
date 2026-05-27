#You are given a list that contains integers.
#You need to decrement each element of the list by 1 and return the list.

n = int(input("Enter the number of element : "))
lst = []
for i in range(n):
    x = int(input(f"Enter element {i+1} : "))
    lst.append(x-1)
print("List after decrementing each element by 1 : ", end = " ")
print(lst)
