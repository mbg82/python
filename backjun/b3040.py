nums=[]

for _ in range(9):
    nums.append(int(input()))

total=sum(nums)

for i in range(9):
    for j in range(i+1,9):
        if total-nums[i]-nums[j]==100:

             result=[]
             for k in range(9):
                 if k!=i and k!=j:
                     result.append(nums[k])

             result.sort()
             for r in result:
                 print(r)