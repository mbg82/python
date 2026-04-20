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
inp= int(input())

match inp:
    case 1:
        print('KOREA')
    case 2:
        print('USA')
    case 3:
        print('CHINA')
    case _:
        print('NO')

#9242
