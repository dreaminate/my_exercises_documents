def prime(x):
    if x<=1:
        return False
    if x<=3:
        return True
    if x %2 ==0 or x %3 ==0:
        return False
    prime_ans=5
    while prime_ans*prime_ans <= x :
        if x %prime_ans ==0 or x%(prime_ans+2) == 0:
            return False
        prime_ans += 6
    return True


#     i=0
#     for i in range(len(prime_anslist)):
#         for j in range(i,len(prime_anslist)):
#             if prime_anslist[i] + prime_anslist[j] == n :
#                 print(f"{n} = {prime_anslist[i]} + {prime_anslist[j]}")
#                 return 
#             else:
#                 continue
    
    

#     """while weishenem buxing"""
#     return False
# x=int(input())
# for p in range (4,x+1):
#     if p %2 ==0:
#         ddd(p)
#     else:
#         continue

# print(prime_anslist)
# for i in range (len (prime_anslist)):
    
#     for j in range(len(prime_anslist)-1,i-1,-1):
        
#         print(i,j)

# prime_anslist=[]
# for num in range(2,x):
#     if prime(num):
#         prime_anslist.append(num)
# def ddd(n):
#     i=0
#     for i in range(len(prime_anslist)):
#         for j in range(len(prime_anslist)-1,i-1,-1):
#             if prime_anslist[i] + prime_anslist[j] == n :
#                 print(f"{n}={prime_anslist[i]}+{prime_anslist[j]}")
#                 return 
#     return False
# p=4
# while p <= x :
#     ddd(p)
#     p+=2

'''def prime(x):
    if x<=1:
        return False
    if x<=3:
        return True
    if x %2 ==0 or x %3 ==0:
        return False
    prime_ans=5
    while prime_ans*prime_ans <= x :
        if x %prime_ans ==0 or x%(prime_ans+2) == 0:
            return False
        prime_ans += 6
    return True
n=int(input())
ans1=2
ans2=3
ans3=5
for x in range (4,n+1):
    if x %2 ==0 :
        if prime(x-ans1):
            print(f"{x}={ans1}+{x-ans1}")
        elif prime(x-ans2):
            print(f"{x}={ans2}+{x-ans2}")    
        else:
            while 1:
                if prime(ans3):
                    if prime(x-ans3):
                        print(f"{x}={ans3}+{x-ans3}")
                        break
                    elif prime(ans3+2):
                        if prime(x-(ans3+2)):
                            print(f"{x}={ans3+2}+{x-(ans3+2)}")
                            break
                    else:
                        ans3 +=6
    else:
        continue'''


'''def ddd(n):
    i=0
    for i in range(len(prime_anslist)):
        for j in range(len(prime_anslist)-1,i-1,-1):
            if prime_anslist[i] + prime_anslist[j] == n :
                print(f"{n}={prime_anslist[i]}+{prime_anslist[j]}")
                return '''









       
                
                                

       
                
            # if prime(x-ans3) is False :
            #     while ans4 <= x:
            #         if prime(ans4):
            #             if prime(x-ans4):
            #                 print(f"{x}={ans4}+{x-ans4}")
            #                 break
            #             else:
            #                 ans4 +=6
            #         else:
            #             continue
            # else:
            #     continue
        
                    


                #     print(f"{x}={ans3}+{x-ans3}")  
                #     break
                # else:
                #     ans3 += 6
                #     while ans4 <= x:
                #         if prime(x-ans4):
                #             print(f"{x}={ans4}+{x-ans4}")
                #             break
                #         else:
                #             ans4 += 6
# while ans3 <= x+7 and ans4 <= x:
#     if prime(ans3):
#         if prime(x-ans3):
#             print(f"{x}={ans3}+{x-ans3}") 
#             break
#         else:    
#             ans3 += 6
#             if prime(ans4):
#                 if prime(x-ans4):
#                     print(f"{x}={ans4}+{x-ans4}")
#                     break
#                 else:
#                     ans4 += 6
#             else:
#                 ans4 += 6
#     else:
#         ans3+=6


# while ans3 <= x:
#     if prime(ans3):
#         if prime(x-ans3):
#             print(f"{x}={ans3}+{x-ans3}") 
#             break
#         else:    
#             ans3 += 6
#             continue
#     else:
#         ans3+=6
# if prime(x-ans3) is False:                   
#     while ans4 <= x :
#         if prime(ans4):
#             if prime(x-ans4):
#                 print(f"{x}={ans4}+{x-ans4}")
#                 break
#             else:
#                 ans4 +=6
#                 continue
#         else:
#             ans4 +=6
               




# def ddd(n):
#     i=0
#     for i in range(len(prime_anslist)):
#         for j in range(len(prime_anslist)-1,i-1,-1):
#             if prime_anslist[i] + prime_anslist[j] == n :
#                 print(f"{n}={prime_anslist[i]}+{prime_anslist[j]}")
#                 return 


x=int(input())
numlist=[i for i in range(x)]
prime_anslist=[]
is_prime=[]
nixu_numlist=numlist[::-1] 
for num in range(x):
    if prime(num):
        prime_anslist.append(num)
        is_prime.append(1)
    else:
        is_prime.append(0)
print(prime_anslist)
print(is_prime)
print(numlist)
print(nixu_numlist)