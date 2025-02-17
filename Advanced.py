list  = ['Dave','James','Adam','Kate','James']
print(list)

mysets = set(list)
print(mysets)
mysets.update(['Grace','Grace'])
print((mysets))

frozen = frozenset(mysets)
print('My frozen sets is',frozen)

frozen.add('yellow')
frozen.update(['yellow','Black'])
# print(seto)







# my_set = {1, 2, 3, 4, 5}
# my_list = list(my_set)
# print(my_list)