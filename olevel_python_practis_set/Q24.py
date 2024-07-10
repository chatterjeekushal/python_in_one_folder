

# wright a python program to count even and odd numbers in a list for example input [4,7,5,64,13,18,22,29,37] the output is count of even numbers is 4 and odd numbers 5

list1=[4,7,5,64,13,18,22,29,37]

print(len(list1))

odd,even=0,0

sum1,sum2=0,0

for num in list1:
    
    if num %2==0:
        even+=1
        sum1=sum1+num
    else:
        odd+=1
        sum2=sum2+num

print("even",even,"even",sum1,"odd",odd,"odd",sum2)