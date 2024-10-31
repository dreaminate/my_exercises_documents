put=input()
num_L=[num for num in put.split()]
n=int(num_L[0])
count=1
t=0
s_list=[]
while count<=len(num_L)-1:
    if count %2 != 0:
        for i in range (int(num_L[count])):
            s_list.append(0)
        count+=1
        i=0
    else:
        for i in range(int(num_L[count])):
            s_list.append(1)
        i=0
        count+=1
s=''.join(map(str,s_list))
while t <= n-1:
    print(s[t*n:n+t*n])
    t+=1