## Advanced Python

#### SETS

```
when a list is converted to set, duplicated are removed, Sets are not
indexed so we can not use indexing to acccess values

list  = ['Dave','James','Adam','Kate','James']
print(list)  -- ['Dave', 'James', 'Adam', 'Kate', 'James']

mysets = set(list)
print(mysets)  --{'Dave', 'Adam', 'Kate', 'James'}

mysets.update(['Grace','Grace'])
print((mysets)) --No Duplicates ({'Kate', 'Grace', 'Dave', 'Adam', 'James'})

frozen = frozenset(mysets)
print('My frozen sets is',frozen)

frozen.add('yellow')
frozen.update(['yellow','Black'])  --error Frozen does not allow updates.
# print(seto)


```
#### Joining Sets
```
africa ={'Nigeria','Ghana','Senegal','Dubai'}

Americas= {'USA','Canada','Mexico','Dubai'}

common = africa & Americas
print(common)

print('All Values :',africa | Americas)
print('All Values :',africa.union(Americas))
print('Remove Common Values',africa-Americas)

```
#### List Comprehensions

```

age = [2,4,6,8,30]
names = ['James','Adam','David','Kate','Yellow']

print(tuple(zip(age,names)))
--((2, 'James'), (4, 'Adam'), (6, 'David'), (8, 'Kate'), (30, 'Yellow'))

val1 = [22,43,60,82,300]
val2 = [2,4,3,2,3]

print(tuple(zip(val1,val2)))
--((22, 2), (43, 4), (60, 3), (82, 2), (300, 3))

val3 = [a/b if a > b else 'Impossible' for a,b in (zip(val1,val2))]
print(val3)

print(val3)
--['Impossible', 10.75, 20.0, 41.0, 100.0, 'Impossible']


age = [2,4,6,8,30]
names = ['James','Adam','David','Kate','Yellow']

new_dict = {names[i]:age[i] for i in range(len(age))}
print(new_dict)
{'James': 2, 'Adam': 4, 'David': 6, 'Kate': 8, 'Yellow': 30}

```







