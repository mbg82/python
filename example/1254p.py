from traceback import print_exception


class BlockBox:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def set_travel_mode(self,hour,min):
        print(str(hour)+'시간'+str(min)+'분 동안 여행 모드 ON')

b1=BlockBox('까망이',200000)
b1.set_travel_mode(2,50)
    

