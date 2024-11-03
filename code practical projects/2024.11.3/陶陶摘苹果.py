a1,a2,a3,a4,a5,a6,a7,a8,a9,a10=map(int,input().split())
c=int(input())
n=0
list1=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
for i in range (len (list1)):
    if c+30>=list1[i]:
        n+=1
    else:
        continue
print(n)