low,hig=map(int,input().split())
long=0
for i in range(low,hig+1):
    i =list(str(i))
    copy=i[:]
    x=len(i)
    duoyu=[]
    for item in copy:
        if item=="2":
            i.remove("2")
            duoyu.append("2")
            if len(duoyu)==1 :
                long+=(x-len(i))
            else:
                continue
        else:
            continue
print(long)
    
            
  


    
   
    



