

# # demo=open("demo.txt","a+")


# # # data=demo.read(5)

# # # data=demo.readline()

# # # data=demo.readlines()

# # # data=demo.write("\nnow i larn rect js ")

# # print(demo.read())

# # data=demo.write("\nabc")

# # print(data)
# # print(type(data))

# # demo.close()




# # # open a file
# file1 = open("demo.txt", "r")

# # read the file
# read_content = file1.read()
# print(read_content)

# # close the file
# file1.close()


# # # over wright a file
# file1 = open("demo.txt", "w")

# # read the file
# read_content = file1.write("hello rana")
# print(read_content)

# # close the file
# file1.close()




# # # append a file
# file1 = open("demo.txt", "a")

# # read the file
# read_content = file1.write("\nhello kushal")
# print(read_content)

# # close the file
# file1.close()



# # read file and over wright text
# file1 = open("demo.txt", "r+")

# # read the file
# read_content = file1.read()
# print(read_content)

# wright_content=file1.write("python,java")

# # close the file
# file1.close()



# # read and over wright
# file1 = open("demo.txt", "w+")

# # read the file
# read_content = file1.read()
# print(read_content)

# wright_content=file1.write("java script")

# # close the file
# file1.close()



# # read and append mode
# file1 = open("demo.txt", "a+")

# # read the file
# read_content = file1.read()
# print(read_content)

# wright_content=file1.write("mongodb database")

# # close the file
# file1.close()



# python end paramiter

# data="hello i am "

# print(data,end=" ")

# print("rana",end=" ")



# with syntax

# with open("demo.txt",'r')as f:
    
#     data=f.read()
    
#     print(data)
    
    

# with open("demo.txt","w")as g:
    
#     wrt=g.write("my data")
    
#     print(wrt)




# Deleting a file

# using the os module 

# module like a code libary is a file written by another programmer that generally has a function we can use


import os

os.remove("demo.txt")








# create a new file "demo.txt" using python .add the following data in it:
    
#     hi eneryone
#  we are learning i/o 
#  using java
#  i like programming in java


