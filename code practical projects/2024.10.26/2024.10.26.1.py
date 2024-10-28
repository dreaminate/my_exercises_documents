
r_num,q_num=int(input().split())
r_list=[num for num in range (r_num)]
num_list=[num for num in range (r_num)]
q_list=[num for num in range (q_num)]
for i in range (r_num):
    r_list[i],num_list[i]=map(input().split())
    num_list[i]=int(num_list[i])
for x in range (q_num):
    q_list[x]=input()
info=dict(zip(r_list,num_list))
for item in q_list:
    if item in r_list:
        print(info[item])
    else:
        print(0)
        
      
# r_1,num_1=input().split()
# r_2,num_2=input().split()
# r_3,num_3=input().split()
# q_1=input()
# q_2=input()
# q_3=input()
# carinfo={r_1:num_1,r_2:num_2,r_3:num_3}
# print(carinfo[q_1])
# print(carinfo[q_2])
# print(carinfo[q_3])



from typing import Mapping
r_num,q_num = map(int,input().split())
cars = {}
for i in range(1,r_num+1):
    car,num = map(str,input().split())
    num_car = int(num)
    if car in cars:
        num_car = cars[car] + num_car
    cars[car]=num_car
for x in range(1,q_num+1):
    your_car = input()
    if your_car in cars:
        print(cars[your_car])
    else:
        print('0')


        









# t_2,num_2=input(),input()
# t_3,num_3=input(),input()
# q_1=input()
# q_2=input()
# q_3=input()
# carinfo={t_1:num_1,t_2:num_2,t_3:num_3}
# print(carinfo[q_1])
# print(carinfo[q_2])
# print(carinfo[q_3])




























































