def add_1(P,Q):
    print(P + Q)

def subtract_1(P,Q):
    print(P - Q)

def multiply_1(P,Q):
    print(P * Q)

def divide_1(P,Q):
    print(P / Q)

print('what function would you like to use')
print('1 for addition')
print('2 for subtraction')
print('3 for multiplication')
print('4 for division')
choice = int(input('1-4'))

print(' what 2 numbers would you like to choose')
num_1 = int(input('first number'))
num_2 = int(input('2nd number'))

if choice == 1:
    print('addition of', num_1, 'and', num_2)
    add_1(num_1,num_2)
elif choice == 2:
    print('subtraction of', num_1, 'and', num_2)
    subtract_1(num_1,num_2)
elif choice == 3:
    print('multiplication of',num_1, 'and', num_2)
    multiply_1(num_1,num_2)
elif choice == 4:
    print('division of', num_1, 'and', num_2)
    divide_1(num_1,num_2)
else:
    print('invalid input')







