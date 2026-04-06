def hamsu(x,a,b,c):
    return (a*x*x+b*x+c)

a,b,c= map(int,input().split())

print(hamsu(2,a,b,c))
print(hamsu(3,a,b,c))
print(hamsu(5,a,b,c))    
