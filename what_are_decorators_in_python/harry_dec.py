
import time

def timer(fun):
    def wraper(*args,**kwargs):
        start="function start"
        print(start)
        result = fun(*args,**kwargs)
        end="function end"
        print(end)
        print(f"{fun.__name__}")  
        return result
    return wraper

@timer
def example_fun(n):
    print(n)


example_fun("hello")



def cache(fun):
    cache_value={}
    print(f"chch value {cache_value}")
    def wrapper(*args):
       print(f"args value {args}")
       if args in cache_value:
           print(f"args value repit {args}")
       result = fun(*args)
       cache_value[args]=result
       return result
    return wrapper



@cache
def long_running_function(a):
     time.sleep(4)
     return a

print(long_running_function(2))
print(long_running_function(2))
print(long_running_function(4))