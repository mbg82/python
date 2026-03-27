#snack = '꿀꽈배기'
#print(len(snack))

#print('꿀꽈배기는\n너무\n맛있어요')

# set1={5,7,6,2,9,0}
# set2={3,4,4,5,6,7}

# print(set1)
# print(set2)
# print(set1.intersection(set2))

# list : 중복 o,순서 o, 수정 o 
# tuple : 중복 o, 순서 o, 수정 X
# set : 중복 x, 순서 x

# my_list=['오예스','몽쉘','초코파이']
# print(my_list[0])
# my_list[0]='빅파이'
# print(my_list)

# my_tuple=('오예스','몽쉘','초코파이')
# print(my_tuple[1])

my_set={'돈가스','보쌈','제육덮밥'}
# print(my_set[1])
# my_set[1]='빅파이'
my_set.add('닭갈비')
print(my_set)
my_set.remove('제육덮밥')
print(my_set)
my_set.clear()
print(my_set)
del my_set
print(my_set)