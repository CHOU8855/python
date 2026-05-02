def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''

    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print('the factorial of 1 is',factorial(1))
print('the factorial of 10 is', factorial(10))
print('the factorial of 60 is', factorial(60))
print('the factorial of 70 is', factorial(70))
print('the factorial of 100 is', factorial(100))
print('the factorial of 56 is', factorial(56))
