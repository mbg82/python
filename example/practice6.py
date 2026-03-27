# yellow_card=0
# foul=True

# if foul:
#     yellow_card+=1
#     if yellow_card==2:
#         print('경고 누적 퇴장')
#     else:
#         print('휴..조심해야지')
# else:
#     print('주의')

# min=19
# if min>20:
#     print('게임 많이 했네?')
#     if min>40:
#         print('당장 안 꺼?')
# else:
#     print('뭐해?')

# for x in range(10):
#     print(f'팔 벌려 뛰기 {x}회')

# for n in range(1,31,10):
#     print(f'{n}번은{n}번부터 {n+9}번까지 모아줘')

# my_list=[1,2,3]
# for x in my_list:
#     print(x)

# my_tuple=(1,2,3)
# for x in my_tuple:
#     print(x)

person={'이름':'나귀욤','나이':7,'키':120,'몸무게':23}    
for v in person.values():
    print(v)

for k in person.keys():
    print(k)

for k,v in person.items():
    print(k,v)

# 구구단 
# for x in range(2,10):
#     for y in range(1,10):
#         print(x,'*',y,'=',x*y)

