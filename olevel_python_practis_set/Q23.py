
# wright a python program to print the sum of series 1 power of 3 + 2 power of 3 + 3 power of 3+ ...n3 till nth term n is the value given by the user

num=int(input("enter the number"))

sum=0

for i in range(1,num+1):
    sum+=i**3
print("the sum of number is",sum)