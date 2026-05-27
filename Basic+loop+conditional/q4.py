'''
Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False.
'''

a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
flag_input = (input("Enter your boolean flag : "))
if(flag_input=="True"):
    flag = True
else:
    flag=False
if( (a>0 or b>0) and flag == False ):
    flag = True
    print(flag)
elif( (a<0 and b<0) and flag == True ):
    print(flag)
else:
    flag = False
    print(flag)