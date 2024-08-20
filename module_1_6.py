#Словари
my_dict = {'Yukie' : 30, 'Yura' : 31}
print(my_dict)

print(my_dict['Yukie'])
print(my_dict.get('ololo', 'Not found'))

my_dict['Leon'] = 3
my_dict.update({'Yason' : 1})
print(my_dict)

del_ =  my_dict.pop('Yura')
print(del_)
print(my_dict)

#Множества
my_set = {2,2,3,3,0}
print(my_set)

my_set.add('str')
my_set.add((1,2,3))
print(my_set)

my_set.discard(0)
print(my_set)