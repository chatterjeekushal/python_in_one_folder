


# docstring is a function definaction 



def func(n):
    '''this function print n square'''
    print(n*2)

func(5)
print(func.__doc__)


# this code retuns none becouse docstring k function ar akdom badai likta hoy nahola sei docstring none retun kora

def fun2(n):
    print('b')
    '''hello'''
    print(n*2)

fun2(7)
print(fun2.__doc__)