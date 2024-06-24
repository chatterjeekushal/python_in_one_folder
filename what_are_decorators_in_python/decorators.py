
import time 

# basic decorators syntax in python

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         result = func(*args,**kwargs)
#         end=time.time()
#         print(f"{func.__name__} ran in {end-start} time")
#         return result
#     return wrapper


# @timer


# def example_func(n):
#     time.sleep(n)
    
# example_func(2)




# example 2



def debug(func):
    def wrapper(*args,**kwargs):
        
        args_value=', '.join(str(arg) for arg in args)
        kwrags_value=', '.join( f"{k}={v}" for k,v in kwargs.items())
        
        print(f"colling :{func.__name__} with args {args_value} and kwrags {kwrags_value}")
        return func(*args,**kwargs)
    
    return wrapper
    

@debug
def greet(name,greeting="hello"):
    print(f"{greeting} , {name}")
    

greet("chai", greeting="hanji chai")