#9696
# name,age=input().split()
# name1,age2=input().split()

# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def check(self):
#         if self.age>=18:
#             return 'adult'
#         else:
#             return 'child'

# p1 = Person(name, int(age))
# p2 = Person(name1, int(age2))

# print(f'{name}({age}) : {p1.check()}')
# print(f'{name1}({age2}) : {p2.check()}')


#9697
p1_name,p1_ab,p1_h=input().split()
p2_name,p2_ab,p2_h=input().split()

class Player():
    def __init__(self,name,ab,h):
        self.name=name
        self.ab=ab
        self.h=h

    def avg(self):
        return self.h/self.ab
        
p1=Player(p1_name,int(p1_ab),int(p1_h))
p2=Player(p2_name,int(p2_ab),int(p2_h))

print(f'name:{p1_name}, AVG:{p1.avg():.3f}, AB:{p1.ab}, H:{p1_h}')
print(f'name:{p2_name}, AVG:{p2.avg():.3f}, AB:{p2.ab}, H:{p2_h}')


