'''
You are given a cubic dice with 6 faces. 
All the individual faces have a number printed on them.
The numbers are in the range of 1 to 6, like any ordinary dice. 
You will be provided with a face of this cube, your task is to guess the number on the opposite face of the cube.
'''
n = int(input("Enter the face of the dice :- "))
if(n==1):
    print("Opposite face of the dice is 6")
elif(n==2):
    print("Opposite face of the dice is 5")
elif(n==3):
    print("Opposite face of the dice is 4")
elif(n==4):
    print("Opposite face of the dice is 3")
elif(n==5):
    print("Opposite face of the dice is 2")
elif(n==6):
    print("Opposite face of the dice is 1")
else:
    print("Not a valid face entered")