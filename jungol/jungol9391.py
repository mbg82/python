h,m=map(int,input().split())

if h >= 12 :
    H=h-12
    print(f'{H} : {m} PM')
elif h<12:
    print(f'{h} : {m} AM')