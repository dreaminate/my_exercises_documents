def prime(x):
    if x<=1:
        return False
    if x==2 or x==3:
        return True
    if x%2 == 0 or x %3 ==0:
        return False
    m=5
    while m*m<=x :
        if x%m == 0 or x % (m+2) == 0 :
            return False
        m += 6
    return True
""""
任何整数都可以表示为
6k、6k±1、6k±2、6k±3、6k±4、6k±5
中的一个   其中k是一个整数。    
除2 3外的所有质数一定在 (6k±1) 或者 (6k±5) 中 
而 6k±5 与 6k±1 mod6 下 同余 1 ，是一个性质。
因此只需检查 6k±1  虽然可能会有合数在里面，但是能保证所有质数都在里面。"""
"""下一个也可以是2,3,5的最小公倍数,以此类推"""
# def prime(x):
#     if x<=1:
#         return False
#     if x<=3:
#         return True
#     if x %2 ==0 :
#         return False
#     prime_ans=3
#     while prime_ans*prime_ans <= x :
#         if x %prime_ans ==0 or x%(prime_ans+2) == 0:
#             return False
#         prime_ans += 4
#     return True
"""下面这个会慢于上面，因为集合更大，步长更小。"""

for i in range(2,101):
    if prime(i) :
        print(i,end="\t")




def prime(x):
    if x<=1:
        return False
    if x<=3:
        return True
    if x %2 ==0 :
        return False
    prime_ans=3
    while prime_ans*prime_ans <= x :
        if x %prime_ans ==0 or x%(prime_ans+2) == 0:
            return False
        prime_ans += 4
    return True













