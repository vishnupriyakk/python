#write a pogram to find sum of digits of numbers from range 100 to 200.and append even sum to even list and odd sum to odd list.
res=[]
for i in range(200,400):
    sum=0
    for digit in str(i):
        sum+=int(digit)

    res.append(sum)


print(res)
even=[]
odd=[]
for j in res:
    if (j % 2) == 0:
        even.append(j)
    else:
        odd.append(j)

print("odd list",odd)
print("even list",even)



#biggest element in a list and print their position
a1=[10,39,30,60,15]
largest=0
for i in a1:
    if i>largest:
        largest=i
print("largest number",largest)
print("position",a1.index(largest))




