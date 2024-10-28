from typing import Mapping
R,Q = map(int,input().split())
cars = {}
for i in range(1,R+1):
    car,num = map(str,input().split())
    num_ = int(num)
    if car in cars:
        num_ = cars[car] + num_
    cars[car]=num_
for j in range(1,Q+1):
    your_car = input()
    if your_car in cars:
        the_num = cars[your_car]
        print(f'{the_num}')
    else:
        print('0')