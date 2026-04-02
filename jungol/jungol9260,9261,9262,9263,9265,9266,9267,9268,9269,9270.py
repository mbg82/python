#9260
# #2~~~~~~~~~~~~~~~~~~~~~~
# x=2

# while x<=50:
#     print(x)
#     x=x+2

# #1~~~~~~~~~~~~~~~~~~
# for x in range(2,51,2):
#     print(x)

# i=0
# while i<50:
#     i+=1
#     if i%2==0:
#         print(i)

#9262
# n=int(input())

# for i in range(5,n+1):
#     print(i)

#9261
# N=int(input())

# print(*range(1,N+1))

#9263
# n=int(input())

# for i in range(5,n+1,2):
#     print(i)

#9265
# n=int(input())

# for i in range(-10,n+1):
#     print(i,end=' ')

#9266
# n=int(input())

# for i in range(10,n+1,10):
#     print(i)

#9267
# n=int(input())

# for i in range(n,0,-1):
#     print(i,end=' ')

# #9268
# n=int(input())

# for i in range(n,4,-1):
#     print(i)

#9269
n=int(input())

for i in range(n,0,-3):
    print(i,end=' ')

#9270
n,m=map(int,input().split())


for i in range(n,m+1):
    print(i)