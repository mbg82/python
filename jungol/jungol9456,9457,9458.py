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
#K = int(input())
#def gap(n):
#    global K
#    return abs(K-n)

#a, b, c = (map(int, input().split()))

#print(gap(a))
#print(gap(b))
#print(gap(c))

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class SuperStar:
#     K = 0

# def GetDiff(n):
#     return abs(n - SuperStar.K)

# SuperStar.K = int(input())
# venus = map(int, input().split())

# print(*(GetDiff(x) for x in venus), sep='\n')


#9458
# a=int(input())

# def num():
#     if a>0:
#         print('positive')
#     elif a<0:
#         print('negative')
#     else:
#         print('zero')

# num()

#````````````````````````````````````````````````
# inp=int(input())

# def get_integer(p):
#     ret=''
#     if p>0:
#         ret='positive'
#     elif p<0:
#         ret='negative'
#     else:
#         ret='zero'

#     return ret

# r=get_integer(inp)
# print(r)

#````````````````````````````````````````````````
# def check_number(n):
#     mapping = {
#         (n > 0): 'positive',
#         (n < 0): 'negative',
#         (n == 0): 'zero'
#     }
#     return mapping[True]

# num = int(input())
# # print(num)
# print(check_number(num))

#9459

gender, age = input().split()
# print(gender, age)

def person(gender, age):
    gender=gender.upper()
    
    if gender == 'M':
        if int(age)>=20:
            return 'MAN'
        else:
            return 'BOY'
    
    if gender == 'F':
        if int(age)>=20:
            return 'WOMAN'
        else:
            return 'GIRL'

result = person(gender,age)
print(result)

#9465

n=int(input())

def sum():

    total=0

    for i in range(1,n+1):
        total+=i

        print(total)

sum()
