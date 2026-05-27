# given an integer N. Find an interger K for which N%K is the largest(1<=K<N)
N = int(input("Enter the value of N : "))
if N>=1:
    K = N//2 + 1
    print(f"Greatest value of 'K' for {N}%K is {K}")
else:
    print("No such value exist")