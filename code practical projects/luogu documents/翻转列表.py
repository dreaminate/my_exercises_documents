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
numlist=[]
primelist=[]
is_prime=[]  
for num in range(0,x+1):
    numlist.append(num)
    if prime(num):
        is_prime.append(1)
        primelist.append(num)
    else:
        is_prime.append(0)
nixu_numlist=numlist[-1::-1]
print(numlist)
print(primelist)
print(is_prime)
print(nixu_numlist)
'''索引对应
'''

