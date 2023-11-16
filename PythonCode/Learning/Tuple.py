my_tuple = (1,2,3,4,5,6)
print(my_tuple.index(5) )
print(len(my_tuple))

#SET -bat bien, ko the lap cac gia tri giong nhau  

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

my_set.add(1000)
print(my_set)

my_set.difference(your_set) # 1 2 3 khong thay doi ma chi chi ra khac o dou

my_set.discard(5) # loai bo phan tu 5 cua set

my_setset.difference_update(your_set) # 1 2 3 co su thay doi 

my_set.intersection(your_set) # 4 5 giao cua A va B

my_set.isdisjoint(your_set) # False vi no chong len nhau

my_set.issubset(your_set) # co phai tap con hay khong False

my_set.issuperset(your_set) # False vi my_set khong phai tap me cua your_set

my_set.union(your_set) # 1 2 3 4 5 6 7 8 9 10 ket hop
my_set | your_set #similar with 'union'