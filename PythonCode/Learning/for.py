for item in 'Hello Ngoc Anh':
    print(item)
for numbers in [1,2,3,4,5,6]:
    print(numbers)

user = {
    'name': 'Ngoc Anh',
    'age': 20,
    'can_fly': False
}

for item in user.values():
    print(item)
for key, value in user.items():
    print(key, value)

my_list = [1,2,3,4,5,6,7,8,9]
counter = 0
for summing in my_list:
    counter = counter + summing 
    print(counter)
print(counter)

my_list = 'what\'s up, bro'
new_list = my_list[::-1]
print(new_list)