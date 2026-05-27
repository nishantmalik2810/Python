# Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables of n1 and n2 and print in a single line.
# Note: Don't add a new line in the end.
n1 = int(input("Enter n1(n1>n2) : "))
n2 = int(input("Enter n2 : "))
n = n1-n2
i=1
while i<=10:
    print(n*i,end=" " if i<10 else "")
    i+=1