#Given a tuple arr , print "True" if all elements of tuple are different otherwise print "False".
#A tuple is a collection of items that are ordered and unchangeable.

a= tuple(input("Enter your tuple (Seprated using space) : ").split(" "))
print("Entered tuple : ",a)
b=set(a)
if(len(b)==len(a)):
    print(True)
else:
    print(False)