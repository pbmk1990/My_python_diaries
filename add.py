print("Python adder")
a='y'
while a == 'y' or a == 'Y':
    x = input("Enter first no:")
    while x.isdigit() == False:
        x=input("Enter a valid first no!:")
    y = input("Enter second no:")
    while y.isdigit() == False:
        y=input("Enter a valid second no!:")
    z=int(x)+int(y)
    print("Sum is:",z)
    a = input("Enter y to continue:")

