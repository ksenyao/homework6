my_dict = {'Katya': 2000, 'Sasha': 2011, 'Nikita': 2004}
print(my_dict)
print(my_dict['Katya'])
print(my_dict.get('Tom', 2024))
my_dict.update({'Sveta': 1975, 'Ken': 1562})
print(my_dict)
del(my_dict['Sveta'])
print(my_dict.pop('Ken'))
my_set = (2, 2, 'aink','aink',True,True)
my_set = set(my_set)
print(my_set)
my_set.update([9, 10])
print(my_set)
my_set.remove('aink')
print(my_set)