p = int(input('enter your first number'))
b = int(input('enter your 2nd number'))
choose = int(input('choose a number 1 = add 2 = subtract 3 = multiply 4 = divide'))

def add (p,b):
    print(p + b)

def subtract (p,b):
    print(p - b)

def multiply (p,b):
    print(p * b)

def divide (p,b):
    print(p / b)

if choose == 1:
    print(add)

if choose == 2:
    print(subtract)

if choose == 3:
    print(multiply)

if choose == 4:
   print(divide)





    