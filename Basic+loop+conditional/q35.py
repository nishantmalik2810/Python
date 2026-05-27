'''
Geek is very fond of patterns. Once, his teacher gave him a star pattern to solve.
He gave Geek an integer n and asked him to build a pattern.

Help Geek to build a star pattern.
for example - 3
  *
 * *
* * *
* * *
 * *
  *
'''
n = int(input("Enter the number : "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)