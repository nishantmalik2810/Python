'''
Juggler Sequence is a series of integers in which the first term starts with a positive integer number a 
and the remaining terms are generated from the immediate previous term using the below recurrence relation:

Juggler Formula

https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/705067/Web/Other/2220ffd2-353d-4b30-b2aa-68fe4047f959_1685087657.png

Given a number n, find the Juggler Sequence for this number as the first term of the sequence until it becomes 1.
'''
def juggler(n):
    i=n
    print(i)
    while i!=1:
        if i%2==0:
           i = int(i**0.5)
           print(i)
        elif i%2!=0:
            i = int(i**1.5)
            print(i)

n = int(input("Enter the first term : "))
juggler(n) 
