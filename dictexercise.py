#convert two list into dictionary
l1=["apple","orange","grape"]
l2=[1,2,3]
new={}
for i in range(len(l1)):
    new.update({l1[i]:l2[i]})

print(new)


#compaign two dictionareis
fruit={'name':'apple','color':'red'}
student={'Name':'abc','rollno':'10'}
fruit.update(student)
print(fruit)


#print the value of physics
dict={"class":{"student":{"name":'mike',"marks":{'physics':70,'history':80,'maths':100}}}}
a=dict['class']['student']['marks']['physics']
print(a)

