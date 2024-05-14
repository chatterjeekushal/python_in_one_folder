
username="kushal"

def func():
    # username="chai"
    print(username)
    
print(username)

func()




x=99

def fun2(y):
    z=x+y
    return z

result =fun2(1)

print(result)




h=99

def fun3():
    global h
    
    h=50
    
fun3()
print(h)



j=99

def fun4():
    j=88
    def f1():
        print(j)
    return f1

myresult=fun4()

myresult()




g=99

def chai(num):
    def actual(g):
        return g**num
    return actual



u=chai(2)
b=chai(3)

print(u(3))
print(b(3))






