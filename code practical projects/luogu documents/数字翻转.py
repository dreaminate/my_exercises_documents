n=input()
if n=="0":
    print(0)
else:
    n=n.lstrip("0")
    list1=list(n)
    if list1[0]=="-":
        list1.remove("-")
        my_string1=''.join(list1[::-1])
        
        print(0-int(my_string1))
    else:
        my_string1=''.join(list1[::-1])
        print(int(my_string1))