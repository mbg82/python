# max=25 # 최대 허용 무게
# weight=0 # 현재 캐리어 무게
# item=3 # 각 짐의 무게

# while weight+item<=max : # 캐리어에 짐을 더 넣어도 되는지 확인
#     weight+=item
#     print('짐을 추가합니다.')
# print(f'총 무게는 {weight} 입니다.')

# drama=['시즌1','시즌2','시즌3','시즌4','시즌5']
# for x in drama:
#     if x=='시즌3':
#         print('재미 없대, 그만 보자')
#         break
#     print(f'{x} 시청')

# drama=['시즌1','시즌2','시즌3','시즌4','시즌5']
# for x in drama:
#     if x=='시즌3':
#         print('재미 없대, 건너뛰자')
#         continue
#     print(f'{x} 시청')

for x in range(10):
    if x % 2==1:
        continue
    print(x)