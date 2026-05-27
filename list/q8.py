#You are given a list numbers that contains integers.
#You need to return two lists, one of even numbers and other of odd numbers.

n = int(input("Enter the number of element : "))
lst = []
odd = []
even = []
for i in range(0,n):
    x = int(input(f"Enter element {i+1} of the list : "))
    lst.append(x)
print("COMPLETE LIST : ",lst)
for j in lst:
    if(j%2==0):
        even.append(j)
    elif(j%2!=0):
        odd.append(j)
print("ODD ELEMENT LIST : ",odd)
print("EVEN ELEMENT LIST : ",even)