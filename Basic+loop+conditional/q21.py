#Create the multiplication table from 1 to 10 for a given number n and return the table as an array.
n = int(input("Enter the number : "))
table =[]
for i in range(1,11):
    table.append(n*i)
print(table)