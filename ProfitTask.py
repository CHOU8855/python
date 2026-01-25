actual_cost = float(input('please enter the actual product prices'))
sale_amount =float(input('the amount of money you will sell it for: '))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print('Total Profit = {0}'.format(amount))
else:
    print('No Profit!')


