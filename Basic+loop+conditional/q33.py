'''
For an integer n, find the number of trailing zeroes in n!.
'''

n = int(input("Enter the number : "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"Factorial for number {n} is {fact}")
c=0
while fact>0 and fact%10==0:
    if(fact%10==0):
        c+=1
    fact=fact//10
print("Trailing zeroes are ",c)