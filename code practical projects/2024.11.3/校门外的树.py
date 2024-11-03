L,m=map(int,input().split())
treelist=[]
for x in range(L+1):
    treelist.append(1)
for i in range(m):
    low,high=map(int,input().split())
    for p in range(low,high+1):
        if treelist[p]!=0:
            treelist[p]=0
        else:
            continue
print(sum(treelist))   


    

