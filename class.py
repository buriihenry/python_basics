class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

p1 = Person("Henry", 36)

print(p1.name)
print(p1.age)

#methods
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age =age

	def myFunc(self):
		print("My name is" + self.name)
p1 = Person("Henry", 36)
p1.myFunc()

#class example 2
class Person:
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
	def printname(self):
		print(self.lname, self.fname)
x = Person("Henry", "Burii")
x.printname()
