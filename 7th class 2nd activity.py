# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dick = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'Jhon', 1: [2, 4, 3]}

my_dict = {'name': 'Jack', 'age': 26}

# Output: Jack
print(my_dict['name']) 
print(my_dict.get('age'))       

#update value
my_dict['age'] = 27
print(my_dict)

# add item
my_dict['address'] = 'Downtown'
print(my_dict)

# remove particuler element
my_dict.pop('age')
print(my_dict)

# access a particuler element
print("Address :", my_dict.get('address'))

#remove all the elements
my_dict.clear()
print(my_dict)