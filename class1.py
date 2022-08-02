class Dog:
    attr1="mammal"
    attr2="dog"

    def fun(self):
        print("I am a", self.attr1)
        print("I am a",self.attr2)
Rodger= Dog()

print(Rodger.attr1)
Rodger.fun()

# Class with __init__ method:

class Person: #Class
    def __init__ (self,name): 
        self.name = name
    def say_hi(self):
        print('Hello, My name is:',self.name)
p= Person('Henry')
p.say_hi()            

# Class 
class Dog:
    animal = 'dog'

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
Bull = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print(Bull.animal)
print(Bull.breed)
print(Bull.color)

print('\nBuzo details')
print(Buzo.animal)
print(Buzo.breed)
print(Buzo.color)

print(Dog.animal)

# Solution 3
class Dog:
    animal = 'dog'

    def __init__(self, breed):
        self.breed = breed

    def setColor(self, color):
            self.color=color
    def getColor(self):
            return self.color
Mike = Dog("pug")
Mike.setColor("brown")
print(Mike.getColor())