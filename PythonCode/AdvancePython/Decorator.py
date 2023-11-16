'''

def hello(func):
    func()
def greet():
    print('still here')

a = 0
print(hello(greet))

#Hight Order Function HOC

def greet(func):
    func()

def greet2(func):
    def func():
        return 5
    return func 




#Decorator 2
def my_decorator(func):
    def wrap_func():
        print('%%%%%%%%')
        func()
    return wrap_func   

@my_decorator
def hello():
    print('helllllllloooo')
@my_decorator
def bye():
    print("seee yaaaa , br")
hello()
bye()


#Decorator 3
def my_decorator(func):
    def wrap_func(*args , **kwagrs):
        print('%%%%%%%%')
        func(*args , **kwagrs)
        print('XXXXXXXX')
    return wrap_func   

@my_decorator
def hello(greeting, hello = ':<'):
    print(greeting, hello)

# hello('Hiiii', 'dawdawd')
# a =my_decorator(hello)
# a('Hiiii', 'dawda')
hello('hiiii')

'''#End
from time import time 
def performance(fn):
    def wrapper(*args, **kwagrs):
        t1 = time()
        result = fn(*args, **kwagrs)
        t2 = time()
        print(f'It take {t2-t1} ms.')
        return result
    return wrapper
@performance
def long_time():
    for i in range(10000000000000):
        i*5

long_time()