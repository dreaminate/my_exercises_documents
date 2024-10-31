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
x=int(input())
prime_anslist=[]
for num in range(2,x):
    if prime(num):
        prime_anslist.append(num)
def ddd(n):
    for j in range(len(prime_anslist)-1,-1,-1):
        if prime(n-prime_anslist[j]):
            print(f"{n}={n-prime_anslist[j]}+{prime_anslist[j]}")
            return 
        else:
            continue
p=4
while p <= x :
    ddd(p)
    p+=2

       

# def prime(x):
#     if x<=1:
#         return False
#     if x<=3:
#         return True
#     if x %2 ==0 or x %3 ==0:
#         return False
#     prime_ans=5
#     while prime_ans*prime_ans <= x :
#         if x %prime_ans ==0 or x%(prime_ans+2) == 0:
#             return False
#         prime_ans += 6
#     return True
# x=int(input())
# prime_anslist=[]
# is_prime=[0,0] 
# for num in range(2,x):
#     if prime(num):
#         prime_anslist.append(num)
#         is_prime.append(1)
#     else:
#         is_prime.append(0)
# def ddd(n):
#     for j in range(len(prime_anslist)-1,-1,-1):
#         if is_prime[n-prime_anslist[j]]:
#             print(f"{n}={n-prime_anslist[j]}+{prime_anslist[j]}")
#             return
#         else:
#             continue
# p=4
# while p <= x :
#     ddd(p)
#     p+=2

    

