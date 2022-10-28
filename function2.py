#function
def name(a,b,c):
    print('the younger child  name is:',b)
name(a='ram',b='tom',c='sita')



#arbitarary

def child(**args):
     print("name is:",args['lname'])
child(name='tom',lname='cruise',age=23,city='kod')

#default parameter

def my_function(country="norway"):
    print("I am from" +country)

my_function()

#passing list as argument
def foodlist(a):
    for x in a:
        print(x)
list=[1,2,3,'a','b','c']
foodlist(list)



