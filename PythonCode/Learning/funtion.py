def say__heloo(name, emote):
    print(f'Hi {name} {emote}')

say__heloo('Nam', 'vui')

def sum(num1 ,num2):
    def another_func(n1, n2):
        return n1+n2
    return another_func

total = sum(10, 20)

print(total)

def super_func(name, *args, i ='hi', **kwagrs ):
    '''
    Rules: params , *agrs , default params, **kwagrs
    '''
    total = 0
    for items in kwagrs.values():
        total +=items
    return sum(args) + total

print(super_func('Ngoc Anh', 1,2,3,4,5, num1=5, num2=10))

x = lambda a: a
print(x)

ini