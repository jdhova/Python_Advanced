

age = [2,4,6,8,30]
names = ['James','Adam','David','Kate','Yellow','Red']

# print(tuple(zip(age,names)))
new_dict = {names[i]:age[i] for i in range(len(age))}
print(new_dict)

val1 = [2,43,60,82,300,2]
val2 = [22,4,3,2,3,32]

print(tuple(zip(val1,val2)))

val3 = [a/b if a > b else 'Impossible' for a,b in (zip(val1,val2))]
print(val3)








# numbers = [2,4,6,8,10]
#
# adds = [n*3 for n in numbers]
# print(adds)



# africa ={'Nigeria','Ghana','Senegal','Dubai'}
#
# Americas= {'USA','Canada','Mexico','Dubai'}
#
# common = africa & Americas
# print(common)
#
# print('All Values :',africa | Americas)
# print('All Values :',africa.union(Americas))
# print('Remove Common Values',africa-Americas)



# person = [
#     {'name': 'James', 'city':' Dallas'},
#     {'name': 'Jude', 'city':' Houston'},
#     {'name': 'Kate', 'city':' Dallas'},
#     {'name': 'James', 'city':' Plano'}
# ]
#
# distinctSet = set()
# for p in person:
#     newVal = (p['city'],p['name'])
#     print(newVal)



    # print(p['name'])



# distinctPerson  = set()
# for p,q in person:
#    distinctPerson.update(p['name','city'])
# print(distinctPerson)






# list  = ['Dave','James','Adam','Kate','James']
# print(list)
#
# mysets = set(list)
# print(mysets)
# mysets.update(['Grace','Grace'])
# print((mysets))
#
# frozen = frozenset(mysets)
# print('My frozen sets is',frozen)
#
# frozen.add('yellow')
# frozen.update(['yellow','Black'])
# # print(seto)







# my_set = {1, 2, 3, 4, 5}
# my_list = list(my_set)
# print(my_list)