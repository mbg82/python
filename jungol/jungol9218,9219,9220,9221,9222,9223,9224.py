# 정올 9223
# n=int(input())

# if 1<=n<=20 and n>10:
#     print('Big')
# else:
#     print('')

# 정올 9224
# n=int(input())

# if n<0:
#     print(n)
#     print('MINUS')
# else:
#     print(n)

#9222
# x=True
# y=False

# a= x and y
# b= x or y
# c= not x
# d= not y

# print(f'x and y -> {a}')
# print(f'x or y -> {b}')
# print(f'not x -> {c}')
# print(f'not y -> {d}')

#9221
# m_age,m_height=map(int,input().split())
# f_age,f_height=map(int,input().split())

# if f_age>m_age and f_height>m_height:
#     print('True')
# else:
#     print('False')

#9220
# a,b,c = map(int,input().split())

# calc= a*b*c-a-b-c

# print(calc)

#9219
# a=int(input())
# b=int(input())

# c=a*2
# d=b-3
# e=c*d

# print('width =',c)
# print('length =',d)
# print('area =',e)

#9218
n,m=map(int,input().split())

a=n/m
b=(n%m)*a

print(int(b))