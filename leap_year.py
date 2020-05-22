
def leap_year(x):
	if x%4==0 and (x%100!=0 or x%400==0):
		print(x," is a leap year")
	else:
		print(x," is not a leap year")
    
print('Python Leap year checker')
x=int(input("Enter the year:"))
leap_year(x)
	
