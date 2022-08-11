
# Sum of two numbers
def add(a, b):
	sum = a + b

	return sum

res = add(10,5)

print(res)

print ('\n')
# Even or ODD Number 

def even_number(n):
	if n % 2 ==0:
		print('Even Number')
	else:
		print('Odd Number')
even_number(19)		


print ('\n')
# Version 2

def is_even(list1):
	even_num=[]
	for n in list1:
		if n % 2==0:
			even_num.append(n)
	return even_num
even_num = is_even([2,3,10,15,20,24,9,62])
print(even_num)		