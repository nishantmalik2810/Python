# A series with same common difference is known as arithmetic series.
# The first term of series is 'a' and common difference is d.
# The series looks like a, a + d, a + 2d, a + 3d, . . .
# Find the sum of series upto nth term.
a = float(input("Enter the first term : "))
d = float(input("Enter the common difference : "))
n = int(input("Enter the A.P term upto which you want to add term : "))

sum = (n/2)*( 2*a + (n-1)*d )
print("A.P is :-- ",end = " ")
for i in range(1,n+1):
    print(a+(i-1)*d,end  = "     " if i<n+1 else "")
print()
print(f"Sum upto {n} term of A.P is {sum}")


 