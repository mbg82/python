class Diff():
    def __init__(self, tall, weight):
        self.tall=int(tall)
        self.weight=float(weight)
    
    def print_info(self):
        print(self.tall,f'{self.weight:.1f}')

h1,w1=input('당신의 키와 몸무게를 입력하세요.').split()
h2,w2=input('친구의 키와 몸무게를 입력하세요.').split()

p1=Diff(h1,w1)
p2=Diff(h2,w2)

# 개별 출력
print(f'my 키: {h1}, 몸무게: {w1}')
print(f'friend 키: {h2}, 몸무게: {w2}')

# 키 계산
t_hab=p1.tall+p2.tall
t_minus=abs(p1.tall-p2.tall)
t_avg=(p1.tall+p2.tall)/2

# 몸무게 계산
w_hab=p1.weight+p2.weight
w_minus=abs(p1.weight-p2.weight)
w_avg=(p1.weight+p2.weight)/2

# 최종 출력
print(f'plus 키: {t_hab}, 몸무게: {w_hab:.1f}')
print(f'minus 키: {t_minus}, 몸무게: {w_minus:.1f}')
print(f'avg 키: {t_avg}, 몸무게: {w_avg:.1f}')

#=======================================================================================
# class Person:
#     def __init__(self, height, weight):
#         self.height = height      # 키 (정수)
#         self.weight = weight      # 몸무게 (실수)

#     # 덧셈 연산자 오버로딩
#     def __add__(self, other):
#         return Person(
#             self.height + other.height,
#             self.weight + other.weight
#         )

#     # 출력용
#     def show(self, name):
#         print(f"{name} 키: {self.height}, 몸무게: {self.weight:.1f}")


# # 입력
# h1, w1 = map(float, input('당신의 키와 몸무게를 입력하세요.').split())
# h2, w2 = map(float, input('친구의 키와 몸무게를 입력하세요.').split())

# # 키는 정수로 처리
# p1 = Person(int(h1), w1)
# p2 = Person(int(h2), w2)

# # 출력
# p1.show("my")
# p2.show("friend")

# # 덧셈
# plus = p1 + p2
# plus.show("plus")

# # 뺄셈
# minus = Person(abs(p1.height - p2.height), abs(p1.weight - p2.weight))
# minus.show("minus")

# # 평균
# avg = Person((p1.height + p2.height) / 2,(p1.weight + p2.weight) / 2)
# avg.show("avg")
