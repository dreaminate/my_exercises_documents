if 1%2==0:
    print(1)
else:
    print(0)
def fibonaci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonaci(n-1)+fibonaci(n-2)
n=int(input())
k=int(input())
for i in range (1,n+1):
    if fibonaci(i)%k ==0:
        break
    else:
        continue 
print(n-n//i)