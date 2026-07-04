weather = (0,0,1,1,1,1)
sunny = 0
rainy = 0
for i in range(0,6):
    if(weather[i]==0):
        rainy+=1
    else:
        sunny+=1

if (sunny>rainy):
    print('good weather')
elif (rainy==sunny):
    print('average weather')
else:
    print('bad weather')