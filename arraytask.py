#find the minimum and maximum element in an array
array=[1,22,37,20,45,15]
a=max(array)
print(a)
b=min(array)
print(b)

#arr[]=(1,5,3,2)
#give a random set of numbers,print them insorted order
array1={1,5,3,2}
b=list(array1)
print(sorted(b))


#write a program to reverse the array
array2=[5,10,15,20,25]
array2.reverse()
print(array2)


#create three arrays and find common elements in these array
array4=[1,2,3,4]
array5=[2,3,6,4]
array6=[3,1,4,7]
set1=set(array4)
set2=set(array5)
set3=set(array6)
n1=set1.intersection(set2,set3)
print(n1)
#using forloop
array4=[1,2,3,4]
array5=[2,3,6,4]
array6=[3,1,4,7]
for i in array4:
    if i in array5 and i in array6:
        print(i)

#find the factorial of a number using array
arr1=[]
