
# wright a python function to find the sum of all numbers between 100 and 500 which are divisible by 2

def consum():
    sum=0
    for i in range(100,501):
        if(i%2==0):
            sum=sum+i
    return sum

print(consum())
