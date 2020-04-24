class Person:
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
	def printname(self):
		print(self.fname, self.lname)

class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.year = year
	def welcome(self):
		print(self.fname, self.lname, self.year)
x = Student("Henry", "Burii", 26)
x.welcome()