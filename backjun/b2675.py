T = int(input())

for n in range(T):
    R, S = input().split()
    
    for i in S:
        for j in range(int(R)):
            print(i, end='')
    print()
