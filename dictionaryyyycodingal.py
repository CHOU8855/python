test_dict = {'Hamza' : 2, 'is' : 2, 'the': 2, 'best':2, 'person':1,}

print('the original dictionary :' + str(test_dict))

K = 2


res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1


print('frequency of k is :' +str(res))