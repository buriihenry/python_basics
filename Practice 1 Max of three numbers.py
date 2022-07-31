#solution 1
a = 20
b = 30
c = 10

print(max(a, b, c))

# Solution 2
def maximum(x, y, z):
    list = [x, y, z]
    return max(list)

x= 10
y= 14
z= 12
print(maximum(x, y, z))

#Solution 3

i= 50
j= 60
k =70
def maximum(i, j, k):
    if(i>j) and (i>k):
        largest=i
    elif (j>i) and (j>k):
        largest=j
    else:
        largest=k
    return largest
print(maximum (i,j,k))