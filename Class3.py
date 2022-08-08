class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage=mileage
ferrari = Vehicle(260,10000)
print(ferrari.max_speed)
print(ferrari.mileage)       

# Class without attributes 
class Vehicle:
    pass