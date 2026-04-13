# class Diff():
#     def __init__(self, tall, weight):
#         self.tall=int(tall)
#         self.weight=float(weight)
    
#     def print_info(self):
#         print(f'{self.tall}, {self.weight:.1f}')

# h1,w1=input('당신의 키와 몸무게를 입력하세요.').split()
# h2,w2=input('친구의 키와 몸무게를 입력하세요.').split()

# p1=Diff(h1,w1)
# p2=Diff(h2,w2)

# # 개별 출력
# print(h1,w1)
# print(h2,h2)

# # 키 계산
# t_hab=p1.tall+p2.tall
# t_minus=abs(p1.tall-p2.tall)
# t_avg=(p1.tall+p2.tall)/2

# # 몸무게 계산
# w_hab=p1.weight+p2.weight
# w_minus=abs(p1.weight-p2.weight)
# w_avg=(p1.weight+p2.weight)/2

# # 최종 출력
# print(f'plus 키: {t_hab}, 몸무게: {w_hab:.1f}')
# print(f'minus 키: {t_minus}, 몸무게: {w_minus:.1f}')
# print(f'avg 키: {t_avg}, 몸무게: {w_avg:.1f}')

#=======================================================================================
class Person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    # 덧셈
    def __add__(self, other):
        return Person(
            self.height + other.height, self.weight + other.weight
        )

    # 뺄셈
    def __sub__(self, other):
        return Person(
            abs(self.height - other.height), abs(self.weight - other.weight)
        )

    # 나누기
    def __truediv__(self, num):
        return Person(
            int(self.height / num), self.weight / num
        )

    # str 오버로딩
    def __str__(self):
        return f'키: {self.height}, 몸무게: {self.weight:.1f}'

    # 기존 show (선택)
    def show(self, name):
        print(f'{name} 키: {self.height}, 몸무게: {self.weight:.1f}')


# 입력
h1, w1 = input('당신의 키와 몸무게를 입력하세요.').split()
h2, w2 = input('친구의 키와 몸무게를 입력하세요.').split()

p1 = Person(int(h1), float(w1))
p2 = Person(int(h2), float(w2))

print('my', p1)
print('friend', p2)

# 연산
print('plus', p1 + p2)
print('minus', p1 - p2)
print('avg', (p1 + p2) / 2)