#You are given a string str, you need to print its characters at even indices(index starts at 0).
str = input("Enter your string : ")
for i in range(0,len(str),2):
    print(str[i],end = "")