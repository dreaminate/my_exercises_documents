from math import sqrt
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
n=int(input())
list1=[]
for i in range(1,n+1):
    if n%i==0:
        list1.append(i)
    else:
        continue
for i in range(len(list1)-1,-1,-1) :
    if i<=1:
        continue
    for x in range(2,int(sqrt(i))+1):
        if i%x==0:
            break
        else:
            print(i)
            break


    # if prime(list1[i]) is True:
    #     print(list1[i])
    #     break
   
# print(list2)
# target_num=list2[0]
# print(target_num)
    

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True





  



        



















