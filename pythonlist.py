fruits=['apple','orange','pinapple','grape','mango', 1,2,3,True,False]
print(fruits[0])
print(fruits[-1])
print(fruits[-4])
print(len(fruits))
# list properties
# list constructor

a=list((1,'orange'))
print(a)
mylist=['a','b','c','d','e','f','g',1,2,3,4,5]
print(mylist[-1])
# list slice
print(mylist[2:5])
print(mylist[2:])
print(mylist[:3])
print(mylist[-5:-1])
print(mylist[-3:-1])
print(mylist[-5:-8])
if 'apple' in mylist:
    print("apple found")
else:
    print("apple is not found")
 # changing value

mylist[0]='apple'
print(mylist)
mylist[2:5]=['orange','grape','banana']
print(mylist)
mylist[2:3]=['b1','b2','b3']
print(mylist)
#insert function
mylist.insert(1,'orange')
print(mylist)


#append function


mylist.append('hello')
print(mylist)

# append element from another list(extend)

mylist.extend(fruits)
print(mylist)

#remove list items(remove function)

mylist.remove('apple')
print(mylist)

#pop function

mylist.pop(0)
print(mylist)

mylist.pop()
print(mylist)

#delete function
del mylist[0]
print(mylist)





