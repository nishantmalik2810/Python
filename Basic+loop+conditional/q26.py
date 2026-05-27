#Given an integer n. Write a program to print all the divisors of n in a single line.
n = int(input("Enter the number : "))
table = []
for i in range(1,n+1):
    if(n%i==0):
        table.append(i)
print(table)