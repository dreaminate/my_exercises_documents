def sum_(n):
    ans2=2*10*(10**n-1)//9
    ans3=(100**(n+1)-100)//99
    return 64*(n+ans3-ans2)//81
n=int(input())
for i in range(1,n):
    print(sum_(n))
    