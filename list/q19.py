'''

You are given an array of integer arr[] where each number represents a vote to a candidate.
Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format.

'''

n = int(input("Enter the number of element : "))
lst = []
for i in range(0,n):
    x = int(input(f"Enter element {i+1} of the list : "))
    lst.append(x)
print("COMPLETE LIST : ",lst)
b = []
for i in lst:
    count = 0
    for j in lst:
        if i == j:
            count+=1
    if count>len(lst)//3:
        b.append(i)
sor = list(set(b))
sor.sort()
print("MAJORITY : ",sor)