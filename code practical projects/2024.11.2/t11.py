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
for i in range(len(lists)):
        if lists[i] in listt:
            record.append(i)
            yuansu.append(lists[i])
        else:
            continue
print(record)
print(listt)
print(yuansu)
print(lists)


