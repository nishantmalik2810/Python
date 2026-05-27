#Given two integers a and b, the task is to compute their LCM and GCD and return an array containing their LCM and GCD.

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = a
d = b
i = 1
gcd = 0
while i <= min(a,b):
    if(a%i==0 and b%i==0):
        gcd = i
    i+=1
lcm = (a*b)//gcd
list = [lcm,gcd]
print(list)
