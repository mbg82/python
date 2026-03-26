# python='파이썬'
# java='자바'

# print('개발 언어에는 {},{} 등이 있어요'.format(python, java))

# print('하지만 \'나만 당할 순 없지\'라는 생각에\"엄청 쉽지\"라고 했다.')

# person={'이름':'나귀욤','나이':7,'키':120,'몸무게':23}
# # print(person['이름'])
# # print(person['나이'])
# # #print(person['별명'])
# # print(person.get('별명')) # 없는 key에 접근하면 None 출력
# # print(person.get('이름')) 
# person['최종학력']='유치원'
# # person['키']=130
# person.update({'키':140,'몸무게':26})
# # person.pop('몸무게')
# # person.clear()
# print(person.keys())
# print(person.values())
# print(person.items())

# my_list=['오예스','몽쉘','초코파이','초코파이','초코파이']
# # my_set=set(my_list)
# # my_list=list(my_set)
# # print(my_list)
# my_dic=dict.fromkeys(my_list)
# print(my_dic)
# my_list=list(my_dic)
# print(my_list)

# today='화요일'
# if today=='일요일':
#     print('게임 한 판')
# else:
#     print('폰 5분만')
# print('공부 시작')

today='수요일'

if today=='일요일':
    print('게임 한 판')
elif today=='토요일':
    print('폰 5분만')
else:
    print('물 한 잔')
print('공부 시작')