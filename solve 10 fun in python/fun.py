
import math

# 1. Basic Function Syntax
# Problem: Write a function to calculate and return the square of a number


def squre(number):
    return number**2

result = squre(4)

print(result)




# 2. Function with Multiple Parameters
# Problem: Create a function that takes two numbers as parameters and returns their sum.


def sum(a,b):
    return a+b

sum_result=sum(2,3)

print(sum_result)



# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings


def multiply(p1,p2):
    return p1*p2

multipy_result=multiply("a",2)


print(multipy_result)



# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.



def circle_stats(radius):
    area= math.floor(math.pi*radius**2)
    circmference = math.floor( 2 * math.pi * radius)
    return area,circmference

a,c=circle_stats(3)

print('area',a,"circmference",c)




# 5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name

def greet(name="user"):
    return "hello" + " " + name


print(greet())



# 06 Lambda Function
# Problem: Create a lambda function to compute the cube of a number.

cube=lambda x:x**3

print(cube(3))



# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value

def print_kwargs(**kwargs):
    for key ,value in kwargs.items():
        print(f"{key}: {value}")
        

print_kwargs(name='rohan',age='20')




# 9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit

def even_generater(limit):
    for i in range(2,limit+1,2):
        yield i


for num in even_generater(10):
    print(num)




# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number

def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)


print(factorial(6))

