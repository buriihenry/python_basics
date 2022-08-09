from ast import Pass


class Person:
    def person_info(self,name,age):
        print('Inside Person class')
        print('Name:',name, 'Age:', age)
class Company:
    def company_info(self,company_name,location):
        print('Inside Company Class')
        print('Name:', company_name, 'location:', location)
#Child Class
class Employee(Person, Company):
    def Employee_info(self, salary,skill):
        print('Inside Employee Class')
        print('Slary:', salary, 'Skill:', skill)
#Object of Employee Class
emp = Employee()

emp.person_info("Henry",28)
emp.company_info('Google', 'Kenya')
emp.Employee_info(700000,'Machine Learning')

# A child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    Pass
School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.mileage)            
