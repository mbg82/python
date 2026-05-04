n = int(input())

arr = [[0]*n for _ in range(n)]

num = 1

for col in range(n):        # 열 기준
    for row in range(n):    # 위 → 아래
        arr[row][col] = num
        num += 1

# 출력
for row in arr:
    print(*row)