
choice=int(input("enter the choice"))
if choice==1:
    m="w"
elif choice==2:
    m="a"
else:
    print("nothing")
f=open("fileprblm.txt",mode=m)
while True:
    a=input("enter a line")
    f.writelines(a)
    f.writelines("\n")
    ch=input("continue y/n")
    if ch=="N":
        break
f.close()