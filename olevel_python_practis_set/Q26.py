
# wright a python program to multiply two numbers by repeated addition

num1=int(input("enter fast number: "))

num2=int(input("enter 2nd number: "))

product=0

for i in range(num2):
    product=product+num1
    print("the multiply is",product)
    

