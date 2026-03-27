#928p
# from operator import is_


# def get_price(): # 함수 정의
#     return 15000

# price = get_price() # 함수 호출

# print(f'커트 가격은 {price}원 입니다.')

#934p
# def get_price(is_vip): # True : 단골손님, False : 일반 손님
#     if is_vip== True:
#         return 10000 #단골손님
#     else : 
#         return 15000 #일반손님

# price=get_price(True)
# print(f'커트 가격은 {price}원 입니다.')
# price=get_price(False)
# print(f'커트 가격은 {price}원 입니다.')

#956p
# def get_price(is_vip=False): # True:단골손님, False:일반손님
#     if is_vip==True:
#         return 10000 #단골손님
#     else:
#         return 15000 #일반손님

# price1=get_price(True) #단골손님
# print(price1)
# price2=get_price() #일반손님
# print(price2)
# price3=get_price() #일반손님
# print(price3)
# price4=get_price() #일반손님
# print(price4)

#1003p
def visit(today,*customers):
    print(today)
    for customer in customers:
        print(customer)

visit('2022년 6월 10일','나장발','티라노사우루스')
visit('2022년 6월 10일','나장발','나수염','나김리','문병권')