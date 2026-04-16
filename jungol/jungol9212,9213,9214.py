#9212
# A = True
# B = False
# C = True

# if A and B:
#     print(True, end=' ')
# else:
#     print(False, end=' ')

# if B or C:
#     print(True, end=' ')
# else:
#     print(False, end=' ')

# if not B:
#     print(True, end=' ')
# else:
#     print(False, end=' ')

#9213
# a= True
# b=False
# c=False

# if not a:
#     print(True)
# else:
#     print(False)

# if a and b:
#     print(True)
# else:
#     print(False)

# if a or b:
#     print(True)
# else:
#     print(False)

# if a and(a or c):
#     print(True)
# else:
#     print(False)

# if a or(a and c):
#     print(True)
# else:
#     print(False)

# if not b or(a and not c):
#     print(True)
# else:
#     print(False)

#9214
# a=0
# b=1
# c=2

# # 1. a and b
# if a and b:
#     print(False, end=' ')
# else:
#     print(True, end=' ')

# # 2. b and c
# if b and c:
#     print(True, end=' ')
# else:
#     print(False, end=' ')

# # 3. a or b
# if a or b:
#     print(False, end=' ')
# else:
#     print(True, end=' ')

# # 4. b or c
# if b or c:
#     print(False, end=' ')
# else:
#     print(True, end=' ')

# # 5. not a
# if not a:
#     print(True, end=' ')
# else:
#     print(False, end=' ')

#92146
a,b,c = map(int,input().split())

if a>b and a>c:
    print(True)
else:
    print(False)

if a == b == c:
    print(True)
else:
    print(False)