'''
Geek is very fond of patterns. Once, his teacher gave him a pattern to solve. He gave Geek an integer n and asked him to build a pattern.

Help Geek to build a star pattern.
for 5 --
*
**
***
****
*****
****
***
**
*
'''
n = int(input("Enter number : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end = "")
    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print("*",end = "")
    print()