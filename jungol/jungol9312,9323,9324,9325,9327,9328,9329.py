#9312
# for i in range(1,10):
#     for gugudan in range(5,8):
#         print(f'{gugudan} * {i} = {gugudan*i}',end='   ')
#     print()



# 9323
# s=int(input())
# e=int(input())

# if s<e:
#     step=1
# else:
#     step=-1

# for i in range(1,10):
#     for j in range(s,e+step,step):
#         print(f'{j} * {i} = {j*i}',end='   ')
#     print()


# if s<=e:
#     for i in range(1,10):
#         for j in range(s,e+1):
#             print(f'{j} * {i} = {j*i}',end='   ')
#         print()
     
# else:
#     for i in range(1,10):
#         for j in range(s,e-1,-1):
#             print(f'{j} * {i} = {j*i}',end='   ')
#         print()


#9324
# for i in range(3):
#     print('*'*(i+1))


#9325
# m=int(input())

# for i in range(m):
    
#     print('*'*(i+1))

#9327
# for i in range(3,0,-1):
#     print('*'*(i))
# for j in range(2,4):
#     print('*'*(j))

#9328
# n=int(input())

# for i in range(n):
#     print('*'*(i+1))
# for j in range(n,0,-1):
#     print('*'*(j))

#9329
n=int(input())

for i in range(n,0,-1):
    print(' '.join('*'*i))
