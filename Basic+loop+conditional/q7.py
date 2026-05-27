#Given a tuple arr with distinct elements and an integer x, find the index position of x.
#Assume to have x in the tuple always. Print the index (0-based).

a = tuple(input("Enter your tuple (Seprated by space) : ").split(" "))
print("Entered tuple : ",a)
x = input("Enter from tuple to check its index : ")
i = 0
c=0
while i<len(a):
    if(a[i]==x):
        print("Index : ",i)
        c=1
    i+=1
if(c==0):
    print("No such element in the tuple")