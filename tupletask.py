#1.Python program to Find the size of a Tuple
tuple=("apple","orange","grape","pappaya")
print(len(tuple))


# #2.Python – Maximum and Minimum K elements in Tuple
tuples=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
max_tuples=(max(tuples))
min_tuples=(min(tuples))
print(max_tuples)
print(min_tuples)



# #3.Create a list of tuples from given list having number and its cube in each tuple
tuple=(1,2,3,4,5)
for i in tuple:
   print(i*i*i)


# #4.Python – Adding Tuple to List and vice – versa
a=[11,12,13,14,15]
tuples=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
tuple1=list(tuples)
add=a+tuple1
add1=tuple1+a
print(add)
print(add1)



# #5.Python – Sum of tuple elements
tuples=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
sum=0
for i in tuples:
   sum=sum+i
print(sum)


#8.Python – Update each element in tuple list
# b1=("apple","orange","grape","pappaya")
# a1=list(b1)
# a1[0:len(a1)]='apple1','orange2','grape3','pappaya4'
# a2=tuple(a1)
# print(a2)

# #Python – Remove Tuples of Length K
t1=[("apple","orange","pappaya"),("grape","pappaya","greengrape","mango"),("dragonfruit","jackfruit","banana","strawberry"),("cherry","blueberry"),]
a=int(input("enter the length:"))
res=[]
for i in t1:
  if len(i)!=a:
      res.append(i)
print(res)




#Python – Remove Tuples from the List having every element as None
l1=[(None),("apple","orange","grape"),(1,2,3,4,5),(None),('a','b','c','d'),(None)]
new=[]
for i in l1:
    if i!=None:
        new.append(i)
print(new)


#python-join tuples if similar initial elements
# t1=[(1,2),(1,3),(4,5),(4,6),(5,6),(5,7),(7,8)]
# res=[]
# for i in t1:
#     if res and res[-1][0]==i[0]:
#         res[-1].append(i[1:])
#     else:
#         res.append([ele for ele in i])
#     res=list(map(tuple,res))
#     print(res)



# #Python – All pair combinations of 2 tuples
t1=(1,2)
t2=(3,4)
new=[(x,y)for x in t1 for y in t2]
new=new+[(x,y)for x in t2 for y in t1]
print(new)




