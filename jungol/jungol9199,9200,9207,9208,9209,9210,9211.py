#9199
# a,b=map(float,input().split())
# c=int(a)

# print(f'{c} + {b} = {a+b}')

#9200
# yard=float(input())

# cm=yard*91.44

# print(f'{yard} yard = {cm} cm')

#9207
# a,b=map(int,input().split())

# c=a%2
# d=b+10

# e=c+d

# print(c,d,e)

#9208
# inp=int(input())
# a,b=map(int,input().split())

# print('True' if inp==a else 'False', end=' ')
# print('True' if inp==b else 'False', end=' ')
# print('True' if inp!=a else 'False', end=' ')
# print('True' if inp!=b else 'False')

#9209
# a,b=map(int,input().split())

# print('True' if a==b else 'False')
# print('True' if a!=b else 'False')

#9210
# a,b,c=map(int,input().split())

# print('True' if a>b else 'False',end=' ')
# print('True' if b>=c else 'False',end=' ')
# print('True' if a<=b else 'False',end=' ')
# print('True' if b<c else 'False')

#9211
x,y = map(int,input().split())

if x>y:
    print(f'{x} > {y} == True')
else:
    print(f'{x} > {y} == False')
if x>=y:
    print(f'{x} >= {y} == True')
else:
    print(f'{x} >= {y} == False')
if x<y:
    print(f'{x} < {y} == True')
else:
    print(f'{x} < {y} == False')
if x<=y:
    print(f'{x} <= {y} == True')
else:
    print(f'{x} <= {y} == False')