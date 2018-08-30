################## Python More on Strings
# explicit convert
print('Chris' + 2) # gives us a traceback
print('Chris' + str(2)) # this will give us a 'Chris2'
# string format language will automatically use a dictionary to fill in the blanks
# in a string statement
sales_record = {'price': 3.24, 'num_items': 4, 'person': 'Chris'}
sales_statement = '{} bought {} items at a price of {} each for a total of {}'
statement = sales_statement.format(sales_record['person'],sales_record['num_items'],
sales_record['price'],sales_record['num_items'] * sales_record['price'])
# this format function will automatically using the parameters to fill in the blanks
# within the statement by order
