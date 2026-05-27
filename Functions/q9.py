'''
Given a positive integer n, return the nth row of pascal's triangle.
Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of previous row.
for 4 row-- 
        1
      1   1
     1  2   1
    1  3  3   1
'''
def pascal(n):
    i = 1
    while i <= n:
        list = []
        for j in range(1,i+1):
            if(j==1 or j ==i):
                list.append(n)
            else:
                list.append(j)
        i+=1
        print(list)
n = int(input("Enter the number of rows in pascal triangle : "))
pascal(n)