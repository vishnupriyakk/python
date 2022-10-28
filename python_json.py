import json
# x='{"name":"priya","age":20,"city":"calicut"}'    #dict purth single cots ittal json aavum
# # print (x(age))
# y=json.loads(x)   #parsing method
# print(y['name'])


#convert from python to json

x1={"name":"priya","age":20,"city":"calicut"}
y1=json.dumps(x1)
print(y1)

print(json.dumps(['apple','banana','orange']))


