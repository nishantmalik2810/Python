#Given an integer n. Write a program to find the first prime number greater than n.
n = int(input("Enter the number : "))
for i in range (n+1,n**2):
    prime = True
    for j in range(2,n+1):
        if(i%j==0):
            prime = False
    if(prime==True):
        print(f"First prime nummber after {n} is {i}")
        break
print("End of code")