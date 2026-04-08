#9377
# str=input()

# print(*str)

#9453
# num=int(input())

# def high():
#     sum=num+10
#     print(f'{num} + 10 = {sum}')
# high()

# def low():
#     minus=num-10
#     print(f'{num} - 10 = {minus}')
# low()

#9378
# str=input()

# print(*str[::2])

#9379
# str=input()

# print(str[::-1])

# # 1.~~~~~
# inp=input().split()
# for x in range(len(inp)-1,-1,-1):
#     print(inp[x],end='')
# #2.~~~~~~
# list1=list(input())
# print("".join(reversed(list1)))
# #3.~~~~~~~
# s = input()
# reversed_str = ""

# for i in range(len(s)):
#     reversed_str = s[i] + reversed_str
# print(reversed_str)


#9382
a='apple orange banana'
b='   Hello world!   '

print(' '.join(reversed(a.split())))
print(b)
print(b.strip())
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#9454
# num1,num2=map(int,input().split())

# def sum():
#     return num1+num2
# print(f'두 수의 합 = {sum()}')

# def minus():
#     if num1>num2:
#         return num1-num2
#     else:
#         return num2-num1
# print(f'두 수의 차 = {minus()}')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# r1,r2=map(int,input().split())
# def calc(p1,p2):
#     sum=p1+p2

#     minus=0
#     if p1>p2:
#         minus=p1-p2
#     else:
#         minus=p2-p1
#         return[sum,minus]

# r1,r2=calc(50,30)
# print(f'두 수의 합 = {calc(r1)}')
# print(f'두 수의 차 = {calc(r2)}')

#9455
# radius=int(input())

# def area():
#     p=radius*radius*3.14
#     print(f'{p:.2f}')
# area()