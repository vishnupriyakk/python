
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
start=2000
stop=3200
def numbers():
    for i in range(start,stop+1):
        if i%7==0 and i%5!=0:
            print(i,end=",")
numbers()






# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such
# that is an integral number between 1 and n (both included). and then the program should print the
#  dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
def dictionary():
    n2 = {}
    for i in range(1,n1+1):
        n2.update({i:i*i})
    print(n2)
n1=int(input("enter the number:"))
dictionary()



#
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
#
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print('factorial of a number',fact)

n1=int(input("enter the number"))
n2=int(input("enter the second number"))
fact(n1)




#
# Write a program which accepts a sequence of comma-separated numbers from
# console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')



def numbers():
    numlist=[]
    while True:
        x=input("what is the number?")
        if x=='none':
            break
        else:

            numlist.append(x)
    print(numlist)
    print(tuple[numlist])
numbers()



#write a program that tests the compatibility between two peaple.(Love Calculator)To work out the love score between two peaple:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs
# 2. Then check for the number of times the letters in the word LOVE occurs.Then combine these numbers to make a two digit number
# *For Love Scores less than 10 or greater than 90, the messages should be :"Your score is **x**,you go together like coke and mentos."
# *For Love Scores between 40 and 50, the message should be :"Your score is **y**,you are alright together."
# EXPL:
# Otherwise, the message will just be their score.e.g.:Your Score is **z**."
# name1="Angela Yu" name2="Jack Bauer"
# T occurs 0 times R occurs 1 time
# U occurs 2 times E occurs 2 times Total=5
# L occurs 1 time o occurs 0 times V occurs o times E occurs 2 times Total=3
# Love score=53



def love_calc():
    name1=str(input("enter the first name"))
    name2=str(input("enter the second name"))
    word1=['t','r','u','e','T','R','U','E']
    word2=['l','o','v','e','L','O','V','E']
    count1=0
    count2=0
    for i in name1:
        if i in word1:
          count1=count1+1
    for i in name2:
        if i in word1:
           count1=count1+1
    for i in name1:
        if i in word2:
            count2=count2+1
    for i in name2:
        if i in word2:
            count2=count2+1
    total=int((str(count1))+(str(count2)))
    if total<10 or total>90:
        print("your score is",total,"you go together like coke and mentose")
    if total>40 and total>50:
        print("your score is",total,"you are alright together")
    else:
        print("your score is",total)


love_calc()

