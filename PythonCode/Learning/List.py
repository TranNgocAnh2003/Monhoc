# List Slicing
amazon_cart = [
    'A',
    ' B',
    ' C',
    ' D'
]
amazon_cart[0] = 'E'
new_cart = amazon_cart[:]
new_cart[0]='Change'
print(new_cart)
print(amazon_cart)


basket = [1 ,2, 3, 4, 5]

basket.insert(3, 100)# cho vao o vi tri cu the
basket.extend([1000, 100003, 199999])
print(basket)

new_list = basket.remove(1)
basket = ['a' , 'e', 'd','b', 'c']

print(basket.index('b', 0, 2)) #truy xuat vi tri
sentences = 'yeu i ai yeu em' 
print(sentences.count('i')) #dem ky tu trong sau

print("                   ")

basket.sort()#sap xep
print(basket)
basket.reverse()# dao nguoc
print(basket)

a, b, c, *other, d = 1,2,3,4,5,6,7,8,9
print(a)
print(b)
print(c)
print(other)

sentence = ' Hi '
new_sentence = sentence.join(' Lien ')
print(new_sentence)