from numpy.ma.extras import average  #list:
items=['beer', 'cigg', 'tacos', 'burritos']
groom=['shower', 'trim nail', 'go bald', 'brush']
print(items)
print(items[1])
print(items[-1])
print("list methods: .append(), insert(), .extend(), .remove(), .pop()")
# by default pop removes the last value from thelist (useful when we wanna use our list like a stack or a queue)
#append adds at end of list, insert for a specific index
items.insert(0, 'fasos')
items.append("thoda-sa-pyaar??")
items.extend(groom)
print(items)
popped=groom.pop(2)
print(groom)
print(popped)
#sorting lists:
items.reverse()
print(items)
items.sort()
print(items)
nums=[1,5,4,2,3]
#nums.sort()
#print(nums)
#nums.sort(reverse=True)
#print(nums)
# we dont have to modify the original list for sorting, for this we can use the sorted function instead of the sort method
temp=sorted(nums)
print(temp)
print('just like sorted there are otehr functions too like min, max, average, sum, etc.')
print(min(nums))
print(max(nums))
print(average(nums))
print(sum(nums))
print('index method can be used to find index of a value, and the in method can be used to check if a value is in the list of not')
print(items.index('beer'))
print('fun' in items)
print('the join method is used to convert a list into a string, and split to convert string to list')
items_str=', '.join(items)
print(items_str)
new_list=items_str.split()
print(new_list)
# tuples:
print("tupes are basically lists that cant be modified, theyre immutable, lists are mutable")
tuple1=('beer', 'cigg', 'tacos', 'burritos')
tuple2=tuple1
print(tuple1)
print(tuple2)
#the below will give typeerror
""" tuple1[0]='gin'
print(tuple1)
print(tuple2)
"""
print('a set contains unordered values with no duplication ')
set1={'beer', 'cigg', 'tacos', 'burritos'}
set2={'beer', 'toothbrush'}
print(set1)
print('sets come with the intersection functionality that you can test what values two or more sets share with each other, two methods to remmeber: intersection, difference, union')
print(set1.intersection(set2))
print(set1.difference(set2))
# empty lists:
list_a=[]
list_b=list()
# empty tuples:
tuple_a=()
tuple_b=tuple()
# empty sets:
set_a={} # this is wrong cuz internally it createsa dict, not a set
set_b=set()

#dictionaries:
print('dictionaries allow us to work with key:value pairs')
healthStat={'sleep':8, 'water':6, 'bmiStatus':'healthy'}
print(healthStat)
print(healthStat['sleep'])
healthStat['weight']=70
print(healthStat.get('weight'))  #get returns none instead of an error when a key doesnt exist
print('update method is used to update values in dicts(it can also add new keys if they dont exist yet)')
healthStat.update({'weight':71,'sleep':4})
print(healthStat)
print('del keyword is used to delete a key from a dict, pop can be used too')
del healthStat['bmiStatus']
print(healthStat)
print('other methods are len(), .keys(), .values(), .items()')
