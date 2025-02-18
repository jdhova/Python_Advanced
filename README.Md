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






