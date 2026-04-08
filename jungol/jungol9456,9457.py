# 9456
# def hamsu(x,a,b,c):
#     return (a*x*x+b*x+c)

# a,b,c= map(int,input().split())

# print(hamsu(2,a,b,c))
# print(hamsu(3,a,b,c))
# print(hamsu(5,a,b,c))    


#9457
# k=int(input())
# l,n,m=map(int,input().split())

# def diff():
#     return abs(l-k)

# def diff1():
#     return abs(n-k)

# def diff2():
#     return abs(m-k)

# print(diff())
# print(diff1())
# print(diff2())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
K = int(input())
def gap(n):
    global K
    return abs(K-n)

a, b, c = (map(int, input().split()))

print(gap(a))
print(gap(b))
print(gap(c))

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class SuperStar:
#     K = 0

# def GetDiff(n):
#     return abs(n - SuperStar.K)

# SuperStar.K = int(input())
# venus = map(int, input().split())

# print(*(GetDiff(x) for x in venus), sep='\n')
