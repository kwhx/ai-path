#for, while
dict1={1,2,3,4,5}
for nums in dict1:
    print(nums)
#break and continue are available in py
#range function in python is veryuseful
for i in range(1,10):
    print(i)

#functions and shi
print('def keyword stands for definition')

def hellow(name='you'):
    print(f'hellow {name}')

hellow()
print('DRY paradigm: dont repeat yourself')

print('positional and keyword arguments are advanced yet imp, *args & **kwargs, used when we want to provide an arbitary num of arguments to the func')

def stu_info(*args, **kwargs):
    print(args)
    print(kwargs)

stu_info('john', 'doe', age=20, sex=True)

def stuinfo2(*args, **kwargs):
    print(args)
    print(kwargs)

name=['john', 'doe']
det = {'age': 20, 'sex': True}
stuinfo2(*name, **det)

