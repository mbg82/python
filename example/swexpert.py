T = int(input())

for i in range(1, T + 1):
    m=list(map(int,input().split()))
           
    result = 0
    for n in m:
        if n%2 == 1:
            result +=n
           
    print(f'#{i} {result}')