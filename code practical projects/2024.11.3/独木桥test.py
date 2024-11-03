a=-1
print(-a)

    



L=int(input().strip())
N=int(input().strip())
if N>L:
    print()
key=[]
value=[]
count=0
for i in range(1,N+1):
    f,s=map(int,input().split())
    key.append(i*f)
    value.append(s)
while len(key)>0:
    list1=value.copy()
    list2=key.copy()
    for i in range(len(key)):
        if value[i] >= L or value[i]<=0:
                del list1[i]
                del list2[i]
        else:    
            continue
    value=list1.copy()
    key=list2.copy()
    if len(value)==0:
        break
    for m in range(len(value)):
        if key[m] <0:
            value[m]-=1
        else:
            value[m]+=1
    count+=1
    for i in range(len(key)-1):
        if value[i]==value[i+1]:
            key[i],key[i+1]=-key[i],-key[i+1]
        else:
            continue
print(count)    