# a='helooooooooooooo'

# if((n:=len(a))>10):
#     print(f'a is too long with {n}')
# while((n:=len(a))>1):
#     a=a[:-1]
# print(a)

# Global KeyWord

# total = 0;

# def count():
#     global total # Goi bien toan cuc cho ham func neu thieu se bi loi,
#                  #khi goi glao bal se reset total cua ca ben ngoai la chay 1 lan count --> total =1
#     total += 1
#     return  total

# count()
# count()
# print(count())

# print(count(count(count(total)))) #-->3 total += 1


# Nonlocal Keyword

# def outer():
#     x= "local"
#     def inner():
#         nonlocal x
#         x = 'nonlocal'
#         print("inner:", x)
#     inner()
#     print("outer:", x)

# outer()
# string = 'Helloo'
# print(string.replace())

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
1357
8

9
