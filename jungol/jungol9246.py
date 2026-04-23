#9246
# A,B,C=map(int,input().split())

# max_val=A if A > B else B
# max_val=max_val if max_val > C else C

# min_val = A if A<B else B
# min_val=min_val if min_val < C else C
# print(max_val - min_val)

#9245
# X=int(input())
# Y=int(input())
# O=input()

# if O == '+' :
#     print(f'ans = {X + Y}')
# elif O == '-' :
#     print(f'ans = {X - Y}')
# elif O == '*':
#     print(f'ans = {X * Y}')
# elif O == '%':
#     print(f'ans = {X % Y}')

#9244

# d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
# month = int(input())

# print(d[month])

#9243
# inp= int(input())

# match inp:
#     case 1:
#         print('KOREA')
#     case 2:
#         print('USA')
#     case 3:
#         print('CHINA')
#     case _:
#         print('NO')

#9242
year = int(input())

if (year % 4 ==0 and year % 100 !=0) or year % 400 == 0:
    print('leap year')
else:
    print('common year')

#9241
# N = int(input())

# if N == 0:
#     print('ZERO')
# elif N > 0:
#     print('PLUS')
# else :
#     print('MINUS')



#9240
# inp1, inp2=map(int,input().split())

# print(max(inp1,inp2)-min(inp1,inp2))

#9239
# a,b,c = map(int,input().split())

# print(a if a<b and a<c else(b if b<c else c))

#9238
# a=int(input())
# b=int(input())

# print(a if a > b else b)
