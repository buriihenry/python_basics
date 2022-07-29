 # Accept a list of 5 float numbers as an input from the user

numbers = []

for i in range (0, 5):
    print("ENter number", i, ":")
    item =float(input())
    numbers.append(item)

print("User List:", numbers)    
