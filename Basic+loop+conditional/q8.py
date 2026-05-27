'''
Given two integers d and n. Where d is the day, out of 7 days of the week, d varies from 0 to 6 as shown below.
0 - Sunday
1 - Monday
2 - Tuesday
3 - Wednesday
4 - Thursday
5 - Friday
6 - Saturday

You have to return the index for the day which is n days before the given day d.
'''
print("0 - Sunday\n1 - Monday\n2 - Tuesday\n3 - Wednesday\n4 - Thursday\n5 - Friday\n6 - Saturday")
d = int(input("Enter the index of the day : "))
n = int(input("Enter the no. of days before 'd' whose index u wanna print : "))
e = d-n
c = e%7
print(f"the index {n} days befor day {d} is {c}")