#Given an array, arr of positive integers.
# Find the third largest element in it.
# Return -1 if the third largest element is not found.

n = int(input("Enter the number of element : "))
lst = []
for i in range(0,n):
    x = int(input(f"Enter element {i+1} of the list : "))
    lst.append(x)
print("COMPLETE LIST : ",lst)
lst.sort(reverse=True)
if n<3:
    print("NO THIRD LARGEST ELEMENT")
else:
    largest = lst[0]
    second_largest = -1
    third_largest = -1
    for i in lst:
        if i<largest:
            second_largest = i
            break
    for i in lst:
        if i<second_largest:
            third_largest = i
            break
    print(third_largest)