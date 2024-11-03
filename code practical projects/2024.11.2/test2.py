# def num(n):
#     if n ==0:
#         return 0
#     else:
#         list0=[]
#         for i in range(n):
#             list0.append('2')
#         str1="".join(list0)
#         m=int(str1)
#         return m
# n=int(input())

# def solve(n):
#     if n ==0:  
#         return 0 
#     else:

#         sumlist=[]
#         for i in range(1,n+1):
#             sumlist.append(num(i))
#         x=sum(sumlist)
#         print(sumlist)
#         return x
# print(solve(n))

# while True:
# 	print(eval(input()))


# def num(n):
#     if n ==0:
#         return 0
#     else:
#         list0=[]
#         for i in range(n):
#             list0.append('2')
#         str1="".join(list0)
#         m=int(str1)
#         return m
n=int(input())
def solve(n):
        list0=[]
        x=0
        for i in range(n):
            list0.append('2')
            str1="".join(list0)
            m=int(str1)
            x+=m
        return x
def solve(n):
    return (2*(10**(n+1)-10-9*n))//81
n=int(input())
print(solve(n))

        
        
      

 
       
        
    
    
    
        
        
    
   


        
        
    
    
            
        

        
