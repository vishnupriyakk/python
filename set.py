set={}
print(type(set))
set={"apple","orange","grape","apple","pappya",1,2,3,2,1,'a','b'}
print(set)
print(type(set))
print(len(set))

#accessing set items
set={"apple","orange","grape","apple","pappya",1,2,3,2,1,'a','b'}
for i in set:
    print(i)

#adding
set={"apple","orange","grape","apple","pappya",1,2,3,2,1,'a','b'}
set.add("red",)
print(set)

#deleting
set={"apple","orange","grape","apple","pappya",1,2,3,2,1,'a','b'}
set.remove(1)
print(set)
set.discard("grape")
print(set)


set1={"apple","orange","grape","apple","pappya",1,2,3,2,1,'a','b'}
set2={"abc","dca"}
set1.update(set2)
print(set1)


set={"apple","orange","grape","apple","pappya",1,2,3,2,1,'a','b'}
list=["abc","dca"]
set.update(list)
print(set)


#join sets
set1={"apple","orange","grape","apple","pappya",1,2,3,2,1,'a','b'}
set2={"abc","dca","apple",'a'}
set3=set1.union(set2)
print(set3)
set1.intersection_update(set2)
print(set1)
set1.intersection(set2)
print(set1)



set1={"apple","orange","grape","apple","pappya",1,2,3,2,1,'a','b'}
set2={"abc","dca","apple",'a'}
set3=set1.symmetric_difference(set2)
print(set3)





#tuple to set
b=("apple","orange","grape","pappaya")
print(set(b))
