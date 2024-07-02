
# chak input number palindrome or not

n=int(input("enter number: "))

temp=n

sum=0

while(n>0):
    p=n%10
    sum=sum*10+p
    n=n//10

if temp==sum:
    print("the given number is palindrom")

else:
    print("the given number is not a palindrom")