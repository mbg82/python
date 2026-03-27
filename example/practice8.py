# products=['JOA-2020','JOA-2021','SIRO-2021','SIRO-2022']
# recall=[] # 리콜 대상 제품 리스트
# for p in products:
#     if p.startswith('SIRO'): # 제품명이 SIRO로 시작하는
#         recall.append(p) 

# print(recall)

# 함수 예제
# def my_function():
#     print('새로운')
#     print('함수를')
#     print('만들었어요') 
# my_function()

def show_price(customer):
    print(f'{customer} 고객님')
    print('커트 가격은 15,000원 입니다.')

customer1='나장발'
show_price(customer1)

customer2='나수염'
show_price(customer2)