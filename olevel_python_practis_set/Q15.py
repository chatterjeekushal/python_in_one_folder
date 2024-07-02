
# wright a python function to find the sum all numbers bettween 100 and 500 which are devide by 2

total=0

for i in range(100,501):
    if i%2==0:
        total=total+i

print(total)    