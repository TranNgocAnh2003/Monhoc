#Pure Function

def multi(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multi([1,2,3]))

#map(), filter(), zip(), reduce()
my_list = [1,2,3,4,5]
your_list = [10, 20, 30, 40, 60, 70] 

from functools import reduce
def multiply_by2(item):
    return item*2 

def check_odd(item):
    return item%2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

# print(list(map(multiply_by2, my_list)))
# print(list(filter(check_odd, my_list)))
# print(list(zip(my_list, your_list)))
print(reduce(accumulator, my_list, 0))

from functools import reduce
my_pets = ['sisi', 'bibi', 'titi', 'carla'] #1 Capitalize all of the pet names and print the list
def capitalize(item):
    return item.upper()
print(list(map(capitalize, my_pets)))

my_strings = ['a', 'b', 'c', 'd', 'e'] #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_numbers = [5,4,3,2,1]
print (list(zip(my_strings, my_numbers)))

scores = [73, 20, 65, 19, 76, 100, 88] #3 Filter the scores that pass over 50%
def check_over_50_percent(item):
    if item > 50:
        return item
print(list(filter(check_over_50_percent, scores)))

def combine_number(acc, num):
    print(acc,num)
    return acc + num

print(reduce(combine_number,(my_numbers + scores),0))
# def accumulator(acc, item):
#     return acc + item

# print(reduce(accumulator, (my_numbers + scores),0))


#Lambda Expressions

 

from functools import reduce
my_list = [1,2,3]

#Form: lambda param: action(param)

def multiply_by2(item):
    return item*2

def check_odd(item):
    return item%2

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(list(filter(lambda item: item > 2, my_list)))
print(reduce(lambda acc, item: item + acc, my_list))

#Test 2
my_list = [5,4,3]

print(list(map(lambda item: item**2, my_list)))

a = [(0,2),(9,9),(4,3),(6,-1)]

a.sort(key=lambda x:x[1])
print(a)



#List, Set, Dictionary Comprehensions: the way to creat quickly list,set, dictionray
my_list  = [char for char in 'hellooo']
my_list2 = [char for char in range(1,10)]
my_list3 = [num**2 for num in range(1,10)]
my_list4 = [num**2 for num in range(1,10) if num %2 == 0]

simple_dict ={
    'a': 1,
    'b': 2
}

my_dict ={key:value**2 for key,value in simple_dict.items()}
my_dict2 = {num:num**2 for num in [1,2,3]}
print(my_dict2)

#Excercise: 

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

duplicates = list(set([value for value in some_list if some_list.count(value) > 1]))
print(duplicates)
