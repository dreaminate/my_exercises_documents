# def fibonaci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibonaci(n-1)+fibonaci(n-2)
n=int(input())
k=int(input())
a=1
b=1
if k==1:
    print(0)
else:
    for i in range (3,n+1):
        a,b=a+b,a
        if a>=2 and a %k ==0:
            break
        else:
            continue
    print(n-n//i)

    
    





    

