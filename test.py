prices = {'apple': '4.3', 'banana': 4.50}

my_purchase = {
    'apple': 1,
    'banana': 6}

grocery_bill = sum(float(prices[fruit]) * float(my_purchase[fruit])
                   for fruit in my_purchase)
print ('I owe the grocer $%.2f' % grocery_bill)