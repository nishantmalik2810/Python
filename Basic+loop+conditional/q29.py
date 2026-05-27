'''
Geek is very fond of patterns. Once, his teacher gave him a pattern to solve.
He gave Geek an integer n and asked him to build a pattern.
for 5--
*****
****
***
**
*
'''
n = int(input("Enter number : "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end = "")
    print()