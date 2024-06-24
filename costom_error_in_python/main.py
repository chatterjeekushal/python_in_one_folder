
#costom error

a=int(input("enter number betwween 5 and 9: "))

if(a<5 or a>9):
    raise ValueError("value sould be between 5 and 9")


b=input("enter your namr: ")

if(len(b)<3 or len(b)>10):
    raise ValueError("name length sould be 10 caractors ")

