
# wright a python program to find the factorial of a given positive number

num=int(input("enter a positive number: "))

fac=1

if num<0:
    print("factorial dose not exist for negative numbers")
elif num==0:
    print("the factorial 0 is 1")
else:
    for i in range(1,num+1):
        fac=fac*i

print(f"{num} factorial is {fac}")
