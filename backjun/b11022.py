a=int(input())
result=[]

for i in range(1,a+1):
    b,c=map(int,input().split())
    result.append(f"Case #{i}: {b} + {c} = {b+c}")

for r in result:
    print(r)
