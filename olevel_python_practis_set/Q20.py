

# wright a python function to find the sum of all numbers between 100 and 500 which are divisible by 2


def add_sum(a,b):
    sum=0
    for i in range(a,b+1):
        if(i%2==0):
            sum=sum+i
    
    print(sum)
    

add_sum(100,500)