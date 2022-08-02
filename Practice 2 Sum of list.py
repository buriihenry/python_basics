#solution for sum
def sum (numbers):
    total =0
    for x in numbers:
        total +=x
    return total
print(sum((8,2,3,0,7)))

#solution for multiplication
def multiply (numbers):
    total =1
    for x in numbers:
        total *=x
    return total
print(multiply((8,2,3,1,7)))

#solution 3
def multi(list):
    total =1
    for i in list:
        total *=i
    return total
list = [8,2,3,1,7]
print(multi(list))  

# 
def test_range(n):
    if n in range(3,9):
        print("The number is in the range")
    else:
        print("The number is out of range")
test_range(10)            
