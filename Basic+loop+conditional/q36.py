'''
You will be given an array A of N non-negative integers.
Your task is to find the rightmost non-zero digit in the product of array elements.
'''
n = int(input("Enter the number of lements you need in an array : "))
list = []
for i in range(1,n+1):
    print(f"Enter element {i} : ",end = "")
    a = int(input())
    list.append(a)
print("Array is ",list)
multiply = 1
for i in list:
    multiply = multiply*i
print("The product of the elements of the array is ", multiply)
while multiply>0:
    if(multiply%10==0):
        pass
    else:
        print("Rightmost non-zero digit in the product of array elements is ",multiply%10)
        break
    multiply//=10
