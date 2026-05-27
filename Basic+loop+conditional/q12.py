#Given three integers a, d and n. Where a is the first term, d is the common difference of an A.P.
#Calculate the nth term of A.P. 
#The nth term is given by an = a + (n-1)d

a = int(input("Enter the first term : "))
d = int(input("Enter the comman difference : "))
n = int(input("Enter which A.P term you want to print : "))

ap = (n-1)*d + a
print(ap)


