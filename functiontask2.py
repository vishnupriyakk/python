
#write a program to find lcm of a number using function

def lcm_calculate(a,b):
    if(a>b):
        largest=a
    else:
        largest=b
    value=largest
    while(True):
        if(largest%a==0 and largest%b==0):
            print("lcm of the numbers:",largest)
            break
        else:
            largest=largest+value


a=int(input("entr the first number"))
b=int(input("enter the second number"))
lcm_calculate(a,b)





#assign a differnt name to function and call the function using the new name
def function():
    print("hlo")

name=function
name()
#generate a python list of all the even numbers b/w 9 to 40 using function


def even(a):
    for i in range(4,9):
        if i%2==0:
            print(i)

n1=[]
even(n1)

