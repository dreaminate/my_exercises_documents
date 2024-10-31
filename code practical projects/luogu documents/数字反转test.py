
# n=input().strip()
# list1=[]
# str_n=list(n)
# if str_n[0]=="-":
#     del str_n[0]
#     list1.append(1)
# if str_n[-1]=="0":
#     str_n.remove("0")
# if len(str_n)==1:
#     if len(list1):
#         x=''.join(str_n)
#         print(0-int(x))
# elif len(str_n)==2:
#     str_n[0],str_n[1]=str_n[1],str_n[0]
#     if len(list1):
#         x=''.join(str_n)
#         print(0-int(x))
# elif len(str_n)>=3:
#     i=0
#     while i <= len(str_n)//2:
#         i += 1
#         str_n[-1-i],str_n[i]=str_n[i],str_n[-1-i]
#     if len(list1):
#         x=''.join(str_n)
#         print(0-int(x.strip()))
#     else:
#         x=''.join(str_n)
#         print(int(x.strip()))
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


        
        








 

    





#         for i in range(0,len(str_n)-2):
#             str_n[i]=str_n[i+1]
#         x="".join(str_n)     
#         print(int(n))
#     else:
#         for i_2 in range(0,len(str_n)-2):
#             str_n[i_2]=str_n[i_2+1]
#         x="".join(str_n)     
#         print(int(n))
# else:
#     if  str_n[0] =="-":
#         for i in range(1,len(str_n)-1):
#             str_n[i]=str_n[i+1]
#         x="".join(str_n)     
#         print(int(n))
#     else:
#         for i_2 in range(0,len(str_n)-1):
#             str_n[i_2]=str_n[i_2+1]
#         x="".join(str_n)     
#         print(int(n))
        
            