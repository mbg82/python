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

N=int(input())

print(*range(5,N+1),sep='\n')

