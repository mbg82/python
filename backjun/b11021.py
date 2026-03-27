a=int(input())
b,c=map(int,input().split() for i in range(a))

sum=b+c

for i in range(a):
    print('Case #',a-=1,':',sum)