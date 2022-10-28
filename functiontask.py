
#write a programe to find the factorial of a number using recursion.
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact = fact*i
    print('factorial of a number', fact)

n1=int(input("enter the number"))
fact(n1)



#write a program to make a calculator add,sub,mul,div,mod


def add(a,b):
    sum=0
    sum=(a+b)
    print('sum of the number is:',sum)



def sub(a,b):
    sub=0
    sub=(a-b)
    print('subtration of the numbers:',sub)




def mul(a,b):
    mul = 0
    mul=a*b
    print('multiplication of the numbers:',mul)



def div(a,b):
    div=0
    div=a/b
    print('division of the numbers:',div)

n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
print("1.add\n2.sub\n3.multiply\n4.division")
choice=int(input("enter your selection"))
if choice==1:
    add(n1,n2)
elif choice==2:
    sub(n1,n2)
elif choice==3:
    mul(n1,n2)
elif choice==4:
    div(n1,n2)
else:
    print("invalid")
