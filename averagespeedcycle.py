cycle1 = 10
cycle2 = 20
cycle3 = 30

sum = ((cycle1+cycle2+cycle3)/3)
print (sum)

if cycle1 >= sum:
    print(' 1st cycling faster than average')
else :
    print(' 1st cycling slower than average')

if cycle2 >= sum:
    print('2nd cycling faster than average')
else :
    print('2nd cycling slower than average')

if cycle3 >= sum:
    print(' third cycling faster than average')
else :
    print(' third cycling slower than average')