# #9460

# def change(a,b):
#     a,b=b,a
#     print(f'함수 내부: a = {a}, b = {b}')
#     return a,b

# a,b = map(int, input().split())

# change(a,b)
# print(f'함수 외부: a = {a}, b = {b}')

# a,b =change(a,b)
# print(f'함수 외부: a = {a}, b = {b}')


#9461
# def inp():
#     global a,b

#     if a>b:
#         a= a//2
#         b=b*2
#     else:
#         a=a*2
#         b=b//2
    
# a,b = map(int,input().split())

# inp()
# print(a,b)

#9465
def plus(n):
    total = 0
    for i in range(1, n+1):
        total+=i
    return total
        
n= int(input())

print(plus(n))