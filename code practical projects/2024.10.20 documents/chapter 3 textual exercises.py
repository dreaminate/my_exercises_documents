x=int(input("请输入你要执行的操作，1是sort()方法，2是sorted()函数，3是reverse()方法，4是len()函数:"))
'''.sort()方法'''
if x==1:
    my_list=["shouxiedecongqian","ai,cunzai","feng","wangyanhuan"]
    my_list_1=my_list.copy()
    my_list_2=my_list.copy()
    my_list_3=my_list.copy()
    my_list_4=my_list.copy()
    my_list_5=my_list.copy()
    my_list_6=my_list.copy()
    my_list.sort()
    my_list_1.sort(reverse=True)#按照字母的逆序排列
    my_list_2.sort(reverse=False)#按照字母的正序排列
    my_list_3.sort(key=len)#按照字符串的长度排列
    my_list_4.sort(key=len,reverse=True)#按照字符串的长度逆序排列
    my_list_5.sort(key=len,reverse=False)#按照字符串的长度正序排列
    my_list_6.sort(key=lambda x:x[1])#按照字符串的第二个字母排列
    print(my_list)
    print(my_list_1)
    print(my_list_2)
    print(my_list_3)
    print(my_list_4)
    print(my_list_5)
    print(my_list_6)

'''sorted()函数'''#sorted()函数不会改变原列表的顺序,临时排序。
if x==2:
    my_list_1=["shouxiedecongqian","ai,cunzai","feng","wangyanhuan"]
    print(my_list_1)
    my_storted_list=sorted(my_list_1)
    print(my_storted_list)
    print(my_list_1)#sorted()函数不会改变原列表的顺序
    print(sorted(my_list_1,reverse=True))#按照字母的逆序排列
    print(sorted(my_list_1,reverse=False))#按照字母的正序排列
    print(sorted(my_list_1,key=len))#按照字符串的长度排列
    print(sorted(my_list_1,key=len,reverse=True))#按照字符串的长度逆序排列
    print(sorted(my_list_1,key=len,reverse=False))#按照字符串的长度正序排列
    print(sorted(my_list_1,key=lambda x:x[1]))#按照字符串的第二个字母排列

'''reverse()方法'''#reverse()方法是将列表中的元素逆序排列,与其他因素无关，单纯反向排列
if x==3:
    my_list_2_2=["shouxiedecongqian","ai,cunzai","feng","wangyanhuan"]
    print(f"原列表是{my_list_2_2}")
    my_list_2_2.reverse()
    print(f"逆序排列后的列表是{my_list_2_2}")
    my_list_2_2.reverse()
    print(f"再次逆序排列后的列表是{my_list_2_2}")

'''len()函数'''
if x==4 :
    my_list_3_3=["shouxiedecongqian","ai,cunzai","feng","wangyanhuan"]
    print(f"原列表是{my_list_3_3}")
    print(f"原列表的长度是{len(my_list_3_3)}")