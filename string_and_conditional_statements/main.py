

# string create in python

str1="this is a string"
str2='rahul'
str3="""this is string"""


# create next line in python

str4="this is a \n string 2" # next line

str5="this is \t python "

print(str4,str5) #tab 


# concatenation in python

mystr1="this is "
mystr2=" python"

print(mystr1+mystr2)


#length function in python
mystr3="collage"

print(len(mystr3))


# .indexing

index="python"

print(index[0])
print(index[1])
print(index[4])

# .slicing

str34="python java"

print(str34[1:4])
print(str34[7:11])

print(str34[:6])#[0:6]
print(str34[7:])#[7:11]

str56="apple"

print(str56[-3:-1]) #pl

print(str56[-5:-2]) #app


str67="i am coder"

# str67.endswith("er") # returns true if styring ends with substr

print(str67.endswith("er"))

print(str67.capitalize()) # capitalize your 1st che

print(str67.replace("o","a")) # replace your string str67.replace("replace from","replace to")

print(str67.find("e")) # retuns 2st index of 1st occurrer

print(str67.count("a")) # cound your string


# practice quation

#wap to input users first name & print its length

userinput=input("enter your name :")

print(len(userinput));


#wap to find the occurrence of "$" in a string

str78="this is $ and usa use $"

print(str78.count("$"))




