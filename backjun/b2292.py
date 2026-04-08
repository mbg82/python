a=int(input())

floor=1
max_floor=1

while a>max_floor:
    max_floor+=6 *floor
    floor+=1

print(floor)