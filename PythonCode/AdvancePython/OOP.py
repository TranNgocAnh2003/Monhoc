class BigOject:
    pass
obj1 = BigOject()
print(type(obj1))


#Creating Our Own Object
class PlayerObject:
    membership = True
    def __init__(self, name, age): # duoc goi moi khi chung ta khoi tao mot doi tuong 
        if PlayerObject.membership:
            self.name = name 
            self.age = age
    def shout(self):
        print(f'My name is {self.name}') # phai khai bao self
        #print(f'My name is {PlayerOnject.name}') cai nay la khong duoc boi vi PlayerObj khong phai la mot thuoc tinh trong class
        return 'oce'
    def run(self, hello):
        print(f'My name is (self.name)')

player1 = PlayerObject('Ngoc Anh', 20)
player2 = PlayerObject('Mai', 21)

player2.attack = 50

print(player1.age) # tra ve gia tri age
#print(player2.run()) # tra ve ham run

print(player1)
print(player2)
print(player2.attack)

print(player1.shout())
print(player2.shout())

print(player1.run('hello'))
print(player2.run('hello'))

#__init__
class PlayerObject:
    membership = True
    def __init__(self, name, age): # duoc goi moi khi chung ta khoi tao mot doi tuong 
        if (age > 18):
            self.name = name 
            self.age = age
    def shout(self):
        print(f'My name is {self.name}') # phai khai bao self
    def run(self, hello):
        print(f'My name is (self.name)')

player1 = PlayerObject('Ngoc Anh',1)
print(player1.shout())


#@classmothod and @staticmethor
class PlayerObject:
    membership = True
    def __init__(self, name, age): # duoc goi moi khi chung ta khoi tao mot doi tuong 
        if (age > 18):
            self.name = name 
            self.age = age
    def shout(self):
        print(f'My name is {self.name}') # phai khai bao self
    @classmethod
    def adding_somethng(cls,num1, num2):
        return num1 + num2
    @staticmethod
    def adding_somethng(num1,num2):
        return num1 + num2

player1 = PlayerObject('Ngoc Anh',1)
print(player1.adding_somethng(2,3))

#Encapsulation - Su dong goi la su rang  buoc du lieu va cac chuc nang thao tca cua du lieu do 
#Abstraction -Su truu tuong la che dau thong tin hao truu tuong hoa thong tin va chi cap quyen truy cap vao nhung thu can thiet
#Private and public self._name = name dau _ bieu thi cho viec day la bien rieng neu ta goi bien o ngoai va in mot bien tuong tu thi no sex cho ket qua o ngoai
class PlayerObject:
    membership = True
    def __init__(self, name, age): # duoc goi moi khi chung ta khoi tao mot doi tuong 
        if (age > 18):
            # self._name = name -->private
            # self._age = age
            self._name = name 
            self._age = age
    def run(self):
        return self 
    def speak(self):
        # print(f'My name is {self._name} and I {self._age} year old') #--> private
        print(f'My name is {self.name} and I {self.age} year old')

player1 =PlayerObject('Ngoc Anh', 20)

# player1.name = '???'
# player1.speak ='Boooo' #-->abstraction
print(player1.speak())


# #Inheritance - Tinh thua ke cho phep cac doi tuong moi tiep nhan cac thuoc tinh cua doi tuong hien co 
class User:
    def sing_in(self):
        print('login')
class Wirazd(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'{self.name} attack {self.power}')
class Acher(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
    def attack(self):
        print(f'{self.name} attack {self.arrows}')

Wirazd1 = Wirazd('Thing Veigar', 1000)
Acher1 = Acher('Ngoc Anh', 200)

# print(Acher1.attack())

# # Cau truc:isinstance(instance, Class) : Xet xem la object nay co phai la thanh phan cua class hay khong
print(isinstance(Wirazd1, Wirazd))


#Polymorphism : Tinh da hinh:
class User:
    def sing_in(self):
        print('login')
    def attack():
        print("do nothing")

class Wirazd(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        User.attack(self)
        print(f'{self.name} attack {self.power}')

class Acher(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'{self.name} attack {self.num_arrows}')

Wirazd1 = Wirazd('Thing Veigar', 1000)
Acher1 = Acher('Ngoc Anh', 30)

# def player_attack(char):
    # char.attack()

# player_attack(Acher1)
for char in [Wirazd1, Acher1]:
    char.attack()


#super()
class User:
    def __init__(self, email):
        self.email = email
    def sing_in(self):
        print('login')
    
class Wirazd(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email) # Cho phep lay cac doi so tu class bac tren la User de su dung
        self.name = name 
        self.power = power
    def attack(self):
        User.attack(self)
        print(f'{self.name} attack {self.power}')
#Introspection- Su tu quan sat: kha nang xac dinh mot doi tuong khi ma dang chay --> dir(object): cung cap tat ca cac thuoc tinh ma doi so co 
wirazd1 = Wirazd('Simon', 100, 'Simon@gmail.com')
print(wirazd1.email)


#Dunder Method
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }
    def __str__(self):
        return (f'{self.color}')

    def __len__(self):
        return 0

    def __call__(self):
        return ("Yess")

    def __getitem__(self, i): 
        return self.my_dict[i]

    def __format__(self):
        return 'IT COOOL'

action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])

#ExtendingList
class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list ))


#MultiInheritance
class User:
    def sing_in(self):
        print('login')

class Wirazd(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'{self.name} attack {self.power}')

class Acher(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
    def check_arrows(self):
        print(f'{self.arrows} is remaining')
    def run(self):
        print('Run very fast')

class HybridBorg(Wirazd, Acher):
    def __init__(self, name, power, arrows):
        Acher.__init__(self, name, arrows)
        Wirazd.__init__(self, name, power)

hb1 = HybridBorg('Name', 50, 100)
print(hb1.check_arrows())
print(hb1.attack())


#MRO-Method Resolution Order- Thu tu phan giai phuong phap
class A:
    num =10

class B(A):
    pass

class C(A):
    # num = 1
    pass

class D(B, C):
    pass
print(D.num)
print(D.__mro__)

#Pets Everwhere
class Pets:
    animal = []
    def __init__(self, animal):
        self.animal = animal
    def walk(self):
        for animal in self.animal:
            print(animal.walk())

class Cat():
    is_cat = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is walking'

class Tom(Cat):
    def sing(self, sound):
        return f'Cat{self.name} \'s sound {sound}'
class Mimi(Cat):
    def sing(self, sound):
        return f'{self.name} is sound {sound}'
class Kitty(Cat):
    def sing(self, sound):
        return f'{self.name} is sound {sound}'

my_cat = [Tom('Tom', 4), Mimi('Mimi', 3),Kitty('Kiity', 1)]
my_pets = Pets(my_cat)
my_pets.walk()





