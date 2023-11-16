my_list = [{
'a' : [1, 2, 4],
'b' : 'Mother F',
'c' : True
},
{
'a': [4,5,6],
'b': 'hello Jame',
'c': False
} ]

print(dictionary['a'])
print(dictionary)

print(my_list[1]['c'])

dictionary = { 
    '123': 'heloo',
    '123': [1,2,3]
}
print(dictionary['123'])



user = {
    'st': 'Ngoc Anh',
    'ss': 'Khoai',
    'age' : 60
}
print(user.get('ssso','Dame'))



user_2 = dict(name = 'Ngoc Anh', age = 20)
print(user_2['age'])
print('              ')
print('st' in  user.keys())
print('shhs' in user.values())
new_user= user.clear()
print(new_user)


print('              ')
print(user.pop('ss'))
print(user.popitem())

print(user.update({'dmae': 55}))
print(user)


            
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"
print(car)