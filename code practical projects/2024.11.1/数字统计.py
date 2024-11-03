low,hig=map(int,input().split())
long=0
for i in range(low,hig+1):
    i =list(str(i))
    copy=i[:]
    x=len(i)
    for item in copy:
        if item=="2":
            i.remove("2")
            long+=(x-len(i))
        else:
            continue
print(long)
    name = "Alice"
print("{:>10}".format(name))  # 右对齐，空格填充
print("{:<10}".format(name))  # 左对齐，空格填充
print("{:^10}".format(name))  # 居中对齐，空格填充
            
            
            
    
