s=input().rstrip()
t=input().rstrip()
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
if len(yuansu)==0:
        print(-1,-1)
else:
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

                
    # print(record)
    # print(yuansu)
    # print(judge)
    # print(j2)
    # print(z)
# elif len(lists)>=len(listt):
#     print(-1,-1)

    

        
    


            # if yuansu[i*len(listt)+j]==listt[j]:
            #     judge.append(i*len(listt)+j)
            # else:
            #     judge=[]
            #     break
   
#    for i in range(len(yuansu)):
        # if yuansu[i] == listt[g]:
        #     judge.append(i)
        #     g=1
        #     while g <=len(listt):
        #         for j in range(i+1,len(yuansu)):
        #             if yuansu[j]==listt[g]:
        #                 judge.append(j)
        #                 g+=1

# p=0
# for num in judge:
#     if num-p>=0:
#         p=num
#     else:
#         continue

# print(record[len(listt)*x],record[len(listt)*(x+1)])           

    
      