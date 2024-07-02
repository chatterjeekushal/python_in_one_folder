
# wright a python program to find the sum of degit of an integer number using while loop

n=int(input("enter the number: "))

sum=0

while(n>0):
    p=n%10
    sum=sum+p
    n=n//10

print("the sum of degit is",sum)



# revarse number using while loop


k=int(input("enter the number: "))

sum1=0

while(k>0):
    p=k%10
    sum1=sum1*10+p
    k=k//10

print("the sum of degit is",sum1)





