student={'name':'anu','roll_no':20,'mark':[80,75,60,85]}
print(len(student))

#accessing the dictionary items
student={'name':'anu','roll_no':20,'mark':[80,75,60,85]}
print(student['name'])

#get method
student={'name':'anu','roll_no':20,'mark':[80,75,60,85]}
print(student.get('mark'))

#accessing keys
print(student.keys())

#adding new field
student={'name':'anu','roll_no':20,'mark':[80,75,60,85]}
student['age']=20
print(student)

#accessing values
student={'name':'anu','roll_no':20,'mark':[80,75,60,85]}
print(student.values())

#print all item in dictionary
student={'name':'anu','roll_no':20,'mark':[80,75,60,85]}
print(student.items())

#updating
student={'name':'anu','roll_no':20,'mark':[80,75,60,85]}
student.update({'name':'priya'})
print(student)

#removing items
student.pop('roll_no')
print(student)
student={'name':'anu','roll_no':20,'mark':[80,75,60,85]}
student.popitem()
print(student)
del student['name']
print(student)
student.clear()
print(student)



#create a new dictionary
fruits={'name':'apple','colour':'red','quantity':10,'size':'small'}
for i in fruits:
    print(fruits[i])


for i in fruits.keys():
    print(i)


for i,j in fruits.items():
    print(i,j)


#making a copy
#1.copy method
new=fruits.copy()
print(new)

#nested dictionaries
main={'student':{'name':'anu','roll_no':20,'mark':[80,75,60,85]},'fruits':{'name':'apple','colour':'red','quantity':10,'size':'small'}}
print(main)

#2.dict method
new1=dict(fruits)
print(new1)
