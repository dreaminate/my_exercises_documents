# def find_shortest_subsequence(S, T):
#     m, n = len(S), len(T)
#     if n > m:
s=input()
t=input()
lists=[]
listt=[]
record=[]
yuansu=[]
judge=[]
j2=[]
for x in s:
    lists.append(x)
for x in t:
    listt.append(x)

if len(lists)<len(listt):
    print(-1,-1)
else:
        for i in range(len(lists)):
            if lists[i] in listt:
                record.append(i)
                yuansu.append(lists[i])
            else:
                continue
        for i in range(len(yuansu)-len(listt)+1):
            if yuansu[i:i+len(listt)]==listt:
                delta=record[i+len(listt)-1]-record[i]
                judge.append(delta)
                j2.append(i)
            else:
                continue
if len(judge)!=0:
    z=min(judge)
    print(f"{record[j2[judge.index(z)]]},{record[j2[judge.index(z)]]+z}")
else:
    print(-1,-1)
    

   

    
