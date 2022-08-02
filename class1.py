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