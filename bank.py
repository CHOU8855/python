print ('Hello welcome to the bank')
total_amount = int (input('how much money do you have'))

Amount =int(input('Please Enter Amount for Withdraw :'))
if Amount <= total_amount:
    note_1 = Amount//100
    note_2 = (Amount%100)//50
    note_3 = ((Amount%100)%50)//10

    print ('notes of 100 pound', note_1)
    print ('notes of 50 pound', note_2)
    print ('notes of 10 pound', note_3)

else:
    print('you dont have enough money')
