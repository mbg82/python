name,age=input().split()

class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age

print(f'My name is {name}.')
print(f'I am {age} years old.')