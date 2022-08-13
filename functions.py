
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

print("\n")
# Version 3
def arithmetic(num1, num2):
	add = num1 + num2
	sub = num1 + num2
	multiply = num1 * num2
	division = num1 / num2

	return add, sub, multiply, division

a, b, c, d = arithmetic(10,2)

print("Add:",a)
print("sub:",b)
print("multi:",c)
print("division:",d)

# Program to find the average marks

def find_average_marks(marks):
	sum_of_marks =sum(marks)
	total_subjects=len(marks)
	average_marks=sum_of_marks/total_subjects
	return average_marks
# Calculate grade and return it.
def	compute_grade(average_marks):
	if average_marks >= 80:
		grade = 'A'
	elif average_marks >= 60:
		grade = 'B'
	elif average_marks >= 50:
		grade = 'C'
	else:
		grade = 'F'
	return grade					 

marks = [80,75,90,64,55]
average_marks = find_average_marks(marks)
print("The Avreage Marks is:", average_marks)	

grade = compute_grade(average_marks)
print("Your grade is:",grade)

# program to add and multiply two numbers
def add(x,y):
	result = x + y
	return result

sum = add( 2, 8)
print(sum)

def multiply(x,y):
	result = x * y
	return result

multi= multiply( 2, 8)
print(multi)

