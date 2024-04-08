

# demo=open("demo.txt","a+")


# # data=demo.read(5)

# # data=demo.readline()

# # data=demo.readlines()

# # data=demo.write("\nnow i larn rect js ")

# print(demo.read())

# data=demo.write("\nabc")

# print(data)
# print(type(data))

# demo.close()




# # open a file
file1 = open("demo.txt", "r")

# read the file
read_content = file1.read()
print(read_content)

# close the file
file1.close()


# # over wright a file
file1 = open("demo.txt", "w")

# read the file
read_content = file1.write("hello rana")
print(read_content)

# close the file
file1.close()


# # append a file
file1 = open("demo.txt", "a")

# read the file
read_content = file1.write("\nhello kushal")
print(read_content)

# close the file
file1.close()



# read file and over wright text
file1 = open("demo.txt", "r+")

# read the file
read_content = file1.read()
print(read_content)

wright_content=file1.write("python,java")

# close the file
file1.close()



# read and over wright
file1 = open("demo.txt", "w+")

# read the file
read_content = file1.read()
print(read_content)

wright_content=file1.write("java script")

# close the file
file1.close()



# read and append mode
file1 = open("demo.txt", "a+")

# read the file
read_content = file1.read()
print(read_content)

wright_content=file1.write("mongodb database")

# close the file
file1.close()