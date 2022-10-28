#1.Python program to interchange first and last elements in a list

list=[1,2,3,4,5,'apple','orange','grape','banana','a','b','c','d','e']
list[0]=('e')
list[-1]=(1)
print(list)

#2.Python program to swap two elements in a list

list=['apple','orange','grape','banana']
temp=list[0]
list[0]=list[1]
list[1]=temp
print(list)


#3.Python – Swap elements in String list


#4.Maximum of two numbers in Python

number=[1,2,3,4,5,6,7,8,9,10]
max_number=max(number)
print(max_number)


#5.Minimum of two numbers in Python
number=[10,20,30,40,50,60]
min_number=min(number)
print(min_number)


#6.Python | Reversing a List
list=['apple','orange','grape','banana']
list.reverse()
print(list)



#7.Python | Count occurrences of an element in a list
list=['apple','orange','grape','banana']
count=list.count('apple')
print(count)


#8.Python Program to find sum and average of List in Python
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sum=0
for i in range(1,len(list)):
    sum=sum+i
print(sum)
avg=0
for i in range(1,len(list)):
    avg=sum/len(list)
print(avg)


#9.Python | Sum of number digits in List

list=[11,12,13,14,15]
res=[]
for i in list:
    sum=0
    for digit in str(i):
        sum+=int(digit)
    res.append(sum)
print(res)

#10.Python | Multiply all numbers in the list
list=[11,12,13,14,15]
mul=1
for i in list:
    mul=mul*i
    print(mul)


#11.Python program to find smallest number in a list
list=[5,10,15,20,25]
min_list=min(list)
print(min_list)


#12.Python program to find largest number in a list

list=[5,10,15,20,25]
max_list=max(list)
print(max_list)


#13.Python program to find second largest number in a list

list=[10,11,12,13,14,15]
list.sort()
print(list[-2])


#14.Python program to print even numbers in a list

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for num in list:
    if num%2==0:
        print(num)


#15.Python program to print all odd numbers in a list
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for num in list:
    if num%2!=0:
        print(num)

#16.Python program to count Even and Odd numbers in a List
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_count=0
odd_count=0
for x in list:
    if x%2==0:
        even_count += 1
    else:
        odd_count += 1
print("even_count",even_count)
print("odd_count",odd_count)

#17.Python program to print positive and negative numbers in a list
list=[-5,-4,-3,-2,-1,0,1,2,3,4,5,]
for x in list:
    if x>=0:
       print("positive number is:",x)
    else:
        print("negative number is:",x)


#