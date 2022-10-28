
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
