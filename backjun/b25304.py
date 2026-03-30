price=int(input()) 
amount=int(input()) 
#print(price)
#print(amount)

sum=0 

for i in range(amount): 
    a,b=map(int, input().split())
    #print(a,b)
    sum+=a*b   

if sum == price:  
    print('Yes')
else:
    print('No')