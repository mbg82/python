#9350
# lst=[]

# for i in range(5):
#     lst.append(map(int,input().split()))

# for i in lst:
#     print(i,end=' ')

#9351
# lst=[]

# for i in range(30):
#     lst.append(int(input()))

# for i in lst:
#     print(i, end=' ')


#9353


# a=['a','b','c','d','e']
# print(a)


# for i in range(len(a)-1,-1,-1):
#     print(a[i],end=' ')


# a=['a','b','c','d','e']
# print(a)

# i = len(a) - 1
# while i >= 0:
#     print(a[i], end=' ')
#     i -= 1
    


# 9354
# lst=[]

# for i in range(5):
#     lst.append(input())

# print(lst)

# for i in lst():
#     print('['+', '.join(f"'{i}'" for i in lst)+']')
#     #print('['+', '.join(i)+']')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
# class ListCollector:
#     def __init__(self, target):
#         self.target = target
#         self.storage = []

#     def collect(self):
#         while len(self.storage) < self.target:
#             item = input()
#             self.storage.append(item)
#         return self.storage

# collector = ListCollector(5)
# print(collector.collect())


#9357
a = []

for _ in range(5):
    a.append(int(input()))

print('[', end='')

for i in range(len(a)):
    print(a[i], end='')
    if i != len(a)-1:
        print(', ', end='')

print(']')

del a[-2:]

print('[', end='')

for i in range(len(a)):
    print(a[i], end='')
    if i != len(a)-1:
        print(', ', end='')

print(']')