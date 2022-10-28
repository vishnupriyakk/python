#Write a program to print multiplication table of a given number
mul=int(input("enter the number"))
b=int(input("entr the range"))
i=0
for j in range(b):
    i=j*mul
    print(j, "*", mul ,"=", i)