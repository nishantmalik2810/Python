'''
Given three integers, a, r and n. Where a is the first term, r is the common ratio of a G.P.
and r is equal to 2.  Calculate the nth term of GP.
The nth term is given by an = a * r(n-1), where r = 2.
'''
a = int(input("Enter the first term : "))
r = 2
print("Common Ratio = 2")
n = int(input("Enter the term of G.P you want to print : "))
gp = 2**(n-1)*a
print(gp)
