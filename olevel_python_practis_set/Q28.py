
# python program to chak if year is a leap year or not

year=int(input("enter year: "))

if(year%400==0) and (year%100==0):
    print(f"{year} is a leap year")
    
elif(year%4==0) and (year%100!=0):
    print(f"{year} is a leap year")
    
else:
    print(f"{year} is not a leap year")