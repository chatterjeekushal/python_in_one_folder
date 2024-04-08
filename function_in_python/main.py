

# function in python


def sum(value1,value2):

    val=value1+value2
    print(val)
    return val


sum(4,4) # invoke sum function


# avrage of 3 numbers

def ava(value1,value2,value3):
    result=(value1+value2+value3)/3
    return result

result=ava(4000,240,167)

print(result)


# python defult paramiter value

def cal_prod(a=2,b=2):
    print(a*b)
    return a*b

cal_prod(4,4)  # if i pass requard argument then defult paramiter value are overright or egnore



# to print the lenght of a list of a paramiter

# print the element of list in a single line

# to find the factorial of n (n is the parameter)

# convart inr to usd


# list1=["kushal","rana","sourov","ragav"]


# def lan_list(data):
#     print(len(data))
    

# lan_list(list1)



# def p_list(data):
#     for x in data:
#         print(x,end=" ")

# p_list(list1)




# def fact(n):
#     i=1
#     fac=1

#     while i<=n:
        
#         fac=fac*i
#         i+=1
#     print(fac)
        


# fact(8)



# def con_usd(inr):
#     result=inr*80
#     return result


# inr=con_usd(1)

# print(inr)









# recursion in python

#when a function calls itself repeatedly

def show(n):
    
    if(n==0):
        
        return
    print(n)
    
    show(n-1)
    print("end")
    



show(5) # 5,4,3,2,1





#recursion

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n
    
print(fact(5))










