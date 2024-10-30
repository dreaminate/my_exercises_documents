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

