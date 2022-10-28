#lambda function
x=lambda a:a+10
print(x(2))
#two parameter
x=lambda a,b:a+b
print(x(2,3))

#nested lambda
def function(n):
    return lambda a:a*n
result=function(2)
print(result(10))

#lambda
def function():
    return lambda a:a*a
result=function()
print(result(10))