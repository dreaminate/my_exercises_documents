def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
a,n,m,x=map(int,input().split())

if x==1 or x==2:
    print(a)
elif x==3:
    print(a*2)
else:
    if x!=n :
        Fibonacci_list=[]
        for i in range(1,n):
            Fibonacci_list.append(Fibonacci(i))
        alist=[]
        i=0
        for i in range(n-4):
            alist.append(Fibonacci_list[i]) 
        alist.insert(0,0)
        xishu_p=sum(Fibonacci_list[0:n-4])
        xishu_a=sum(alist[0:n-4])+2
        p=int((m-xishu_a*a)/xishu_p)
        print((sum(alist[0:x-3])+2)*a+sum(Fibonacci_list[0:x-3])*p)
    if x==n :
        print(0)



# a,n,m,x=map(int,input().split())
# ans=1
# Fibonacci_list=[]
# up=0
# uplist=[]
# d=0
# dlist=[]
# for i in range(1,n):
#     Fibonacci_list.append(Fibonacci(i))
# for j in range(2,n):
#     up=Fibonacci_list[j-2]*a+Fibonacci_list[j-1]
#     uplist.append(up)
# dlist=uplist[:]
# dlist.insert(0,1)
# del dlist[-1]
# del dlist[-1]
# person=sum(dlist)+2*a
# xishu_p=sum(Fibonacci_list[0:n-3])
# xishu_a=sum(Fibonacci_list[1:n-3])+2
# p=(m-xishu_a*a)/xishu_p
# print(Fibonacci_list[x-3]*a+Fibonacci_list[x-2]*p)
# print(int(Fibonacci_list[x-3]*a+Fibonacci_list[x-2]*p))





# print(Fibonacci_list,alist,xishu_a,xishu_p,sum(alist[0:x-3]),sum(Fibonacci_list[0:x-3]),p)





# dlist=uplist[:]
# dlist.insert(0,1)
# del dlist[-1]
# del dlist[-1]
# person=sum(dlist)+2*a
# for j in range(2,n):
#     up=Fibonacci_list[j-2]*a+Fibonacci_list[j-1]