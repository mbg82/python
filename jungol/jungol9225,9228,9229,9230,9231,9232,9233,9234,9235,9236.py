#9225
# a=int(input())
# b=int(input())

# print(a+b)

# if a%2==1 or b%2==1:
#     print('ODD')

#9228
# score=int(input())

# if score>=60:
#     print('PASS')
# else:
#     print('FAIL')

#9229
# age=int(input())

# if age<13:
#     print("Elementary School")
# else:
#     print("Middle School")

#9230
# time=int(input())

# if time <12:
#     print('AM')
# else:
#     print('PM')

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# hour = int(input())
# # print(hour)
# is_pm = bool(hour // 12)
# print("PM" if is_pm else "AM")

#9231
# inp=int(input())

# if 90<=inp<=100:
#     print('A')
# elif 80<=inp<=89:
#     print('B')
# elif 70<=inp<=79:
#     print('C')
# elif 60<=inp<=69:
#     print('D')
# else:
#     print('F')


# score=int(input())

# match score // 10:
#     case 10 | 9:
#         print('A')
#     case 8:
#         print("B")
#     case 7:
#         print("C")
#     case 6:
#         print("D")
#     case _:   # default와 같은 
#         print('F')


# score = int(input())

# criteria = {90: "A", 80: "B", 70: "C", 60: "D"}

# result = "F"
# for point, grade in criteria.items():
#     if score >= point:
#         result = grade
#         break

# print(result)


#9232
# weight=float(input())

# if weight<=50.80:
#     print('Flyweight')
# elif weight<=61.23:
#     print('Lightweight')
# elif weight<=72.57:
#     print('Middleweight')
# elif weight<=88.45:
#     print('Cruiserweight')
# else:
#     print('Heavyweight')


#9233
# dice1=int(input())
# dice2=int(input())

# if dice1 >=3 and dice2>=3:
#     print('High')
# elif dice1 >=3 or dice2>=3:
#     print('Mid')
# elif dice1 < 3 or dice2 <3:
#     print('Low')

#9234
# X,Y = map(float,input().split())

# if X >= 4.0 and Y >= 4.0:
#     print('A grade')
# elif X >= 3.0 and Y >= 3.0:
#     print('B grade')
# else:
#     print('F grade')

#9235
# a,b,c = map(int,input().split())

# print(f'MAX: {max(a,b,c)}')

#9236
gender, age = input().split()
age = int(age)

if gender == 'M':
    print("MAN" if age >= 19 else "BOY")
else:
    print("WOMAN" if age >= 19 else "GIRL")