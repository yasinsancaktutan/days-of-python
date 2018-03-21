# take comma separated values from user and put them in a list first then a tuple. Then print them both.

values = input('Give me some comma separated values')
list = values.split(',')
tuple = tuple(list)
print(list, tuple)