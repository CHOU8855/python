print('All marks you got in the five subjects')

markOne = int(input())

markTwo = int(input())

markThree = int(input())

markFour = int(input())

markFive = int(input())

total = markOne+markTwo+markThree+markFour+markFive

avg = total/5

print('your grade is is', avg)

if avg >=91 and avg<=100:
    print('your grade is Exceptional')
elif avg >=81 and avg>= 91:
    print('your grade is Very Good.')
elif avg >=71 and avg>= 81:
    print('your grade is good.')
elif avg >=61 and avg>= 71:
    print ('your grade is satisfactory')
elif avg >=51 and avg>=61:
     print ('your grade is working towards satisfactory')
else:
    print('Your grade is failing and a retake is neccecary')