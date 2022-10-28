fruits=("apple","0range","banana","grape")
print (type(fruits))
print (len (fruits))

#print 1 to 4 numbers
number=(1,2,3,4)
print(number)

#change first value in tuple
fruits=("apple","0range","banana","grape")
a=list(fruits)
a[0]="kiwi"
print(a)


#append new item in tuple
fruits=("kiwi","0range","banana","grape")
a=list(fruits)
a.append("apple")
print(a)

#add a tuple element
fruits=("kiwi","0range","banana","grape")
y=("apple","pappaya",)
fruits +=y
print(fruits)


#remove the element
fruits=("kiwi","0range","banana","grape")
a=list(fruits)
a.remove("grape")
print(a)

#pop
fruits=("kiwi","0range","banana","grape")
a=list(fruits)
a.pop(0)
print(a)

# print tuples
fruits=("kiwi","0range","banana","grape")
for i in fruits:
    print(i)


#multiple the tuple
fruits=("kiwi","0range","banana","grape")
multiple=fruits*2
print(multiple)


#count method
fruits=("kiwi","0range","banana","grape","kiwi","kiwi")
print(fruits.count("kiwi"))

#count using forloop
fruits=("kiwi","0range","banana","grape","kiwi","kiwi")
for i in fruits:
    print(fruits.count(i))
