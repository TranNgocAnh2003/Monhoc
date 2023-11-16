# # i = 0
# # count = 0;
# # while i < 50:
# #     i = i + 1
# #     print(i) 

# picture = [
# [0,0,0,1,0,0,0],
# [0,0,1,1,1,0,0],
# [0,1,1,1,1,1,0],
# [1,1,1,1,1,1,1],
# [0,0,0,1,0,0,0],
# [0,0,0,1,0,0,0]
# ]

# for i in picture: 
#     for j  in i:
#         if (j == 1):
#             print('*', end=(''))
#         else:
#             print(' ', end = (' '))
#     print('')

# input = 

# some_list = ['a','b','c','d','e','f','g','b','a']

# duplicated = []
# for value in some_list:
#     if (some_list.count(value) == 1):
#         if value not in duplicated:
#             duplicated.append(value)
# print(duplicated)

# picture = [
# [0,0,0,1,0,0,0],
# [0,0,1,1,1,0,0],
# [0,1,1,1,1,1,0],
# [1,1,1,1,1,1,1],
# [0,0,0,1,0,0,0],
# [0,0,0,1,0,0,0]
# ]

# for row in picture:
#     for pixel in row:
#         if pixel:
#             print('X', end=(''))
#         else:
#             print(' ', end=(''))
#     print('')

# def age():
#     while True:
#         x = int(input('What is your age?: '))
#         if ( x > 18 ):
#             print('That oce!')
#         elif(x < 18):
#             print('You are not allow.')
#         else:
#             print('No thing to say.')

# age()

# def test(a):
#     '''
#     Info: This func is test the pramater a
#     '''
#     print(a)

#      help(test)
#     print(test.__doc__)

'''CLENCODE'''
def is_odd_or_even(num):
    return num % 2 == 0
    # if num % 2 == 0:
    #     print('even') 
    #     return True
    # elif num % 2 != 0:
    # else
    # print('odd')
    # return False
# print(is_odd_or_even(5))
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:4])
