
# python program to find sum of natural number

num=int(input("enter the number: "))

if num<0:
    print("Input must be a non-negative integer.")
else:
    total=0
    for i in range(1,num+1):
        total=total+i
print(f"total of natural num is {total}")