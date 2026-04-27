# for x in range(1,101):
#     print(x,end=' ')


# for x in range(5,2001,5):
#     print(x,end=' ')


#9255
# import time 

# now =time.localtime()
# a=0
# a=now.tm_year-1900
# a+= now.tm_mon-1
# a+=now.tm_mday
# print(0,126,156)


#9254
# a,b=map(int,input().split())

# print(a+b)
# print(a*b)

#9253
# a,b=map(int,input().split())

# c=max(a,b)-min(a,b)

# print(c)

#9252
# a=5 
# a+=10
# a=a-1
# print(15)

#9251
# score=int(input())

# if score >=90:
#     print('Perfect')
# elif 80 <= score < 90:
#     print('Great')
# else:
#     print("Effort")

#9250
name1, age1=input().split()
name2, age2=input().split()

age1=int(age1)
age2=int(age2)

if age1 > age2:
    print(name1)
else:
    print(name2)