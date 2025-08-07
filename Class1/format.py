name = ['kevin','Mary','Eason']
age = [18, 9, 101]
print('My name is %-6s, I am %3d years old'%(name[0], age[0]))
print('My name is {0:5s}, I am {1:3d} years old'.format(name[1], age[1]))
print(f'My name is {name[2]:5s}, I am {age[2]:3d} years old')
a = 3.1415926
print(f'{a:3f}')