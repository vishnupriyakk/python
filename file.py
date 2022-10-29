# f=open("text.txt",mode="r")
# f.seek(3)
# print(f.tell())
# print(f.read())
# # print(f.readline())
# f.close()




# ##
# f1=open("text.txt",mode="w")
# f1.writelines("vishnupriyakk")
# f1.writelines("roshna")
# f1.writelines("anuradhakrishnan")
# f1.close()

# f2=open("text.txt",mode="r")
# print(f2.read())
# f2.close()

#
# f=open("newtext.txt","x")
# f.close()


#
# f3=open("newtext.txt","w")
# f3.writelines("abcd")
# f3.writelines("efgh")
# f3.writelines("ijkl")
# f3.close()

#
# f4=open("newtext.txt","r")
# f4



import os
# os.remove("newtext.txt")


if os.path.exists("newtext.txt"):
    os.remove()
else:
    print("there is no such file")