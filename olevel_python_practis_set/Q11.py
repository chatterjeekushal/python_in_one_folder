
#wright a python program to input two numbers as input and compute the greatest common devicer

a=int(input("enter the number: "))
b=int(input("enter the number: "))

while(b!=0):
    temp=b
    b=a%b
    a=temp

print(a)