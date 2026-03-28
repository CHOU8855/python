Number = int(input('enter any number: '))
sum = 0
temp = Number
while(temp > 0):
    Factorial = 1

    i = 1
    remainder = temp % 10

    while (i <= remainder):
        Factorial = Factorial * i
        i = i + 1

    print('\n Factorial of %d = %d' %(remainder, Factorial))
    sum = sum + Factorial
    temp = temp // 10

print('\n sum of factorials of a given number %d = %d' %(Number, sum))

if (sum == Number):
    print(' %d is a strong number'%Number)

else:
    print(' %d is not a strong number'%Number)