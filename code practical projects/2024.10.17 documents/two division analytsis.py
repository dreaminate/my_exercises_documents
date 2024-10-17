import random
def division(num1,num2):
    return (num1+num2)/2
    ''' 两个数相加再除2'''

width_longest=int(input("Enter the maxium number of the range: "))
lower_num=1
guess_count=0
times_list=[]
width_list=[]
# cleaned_times_list=[]
if width_longest <20:
    print("The number is too small,no less than 20.")
elif width_longest >=20:
    for i in range(5,width_longest+1):                      #这个for循环，实现上限的变化，对应不同的上限，产生对应预测次数。
        random_maxium = i                                    #这个for循环，填充自变量width_list列表
        if random_maxium<=width_longest :
            width_list.append(random_maxium)
        while random_maxium<=width_longest:                  #这里是为了控制循环次数，不然会无限循
            higher_num=random_maxium                         #这个while循环，实现二分法,并填充因变量times_list列表
            lower_num=1                                      #要好好体会一下这个循环的逻辑
            guess_count=0
            right_num = random.randint(1,random_maxium)
            guess_num = random.randint(1,random_maxium)
            while True:
                if guess_num > right_num:
            
                    higher_num = guess_num
                    guess_num =division(guess_num,lower_num)
                    guess_count+=1
                elif guess_num < right_num:
                    lower_num = guess_num
                    guess_num =division(guess_num,higher_num)
                    guess_count+=1
                else:
                    times_list.append(guess_count)          #填充因变量times_list列表
                    if random_maxium==width_longest:
                        random_maxium+=1                    #为了控制循环次数，不然会无限循环
                    break
            break                                           #一定要小心循环套循环的问题，不然会无限循环
    print(width_list,end="\n\n\n\n\n\n\n")                                       
    print(times_list)
    '''到这里都只是收集数据，下面是数据处理'''



    '''2024.10.17
            码后反思：先构建好思维，什么东西应该在前，什么应该在后要清晰，可以在码代码的时候拿一张纸，标清优先级

            本人不会数据分析，所以这里只是简单的数据处理
            成就感拉满，数据收集成功'''
                                                                            



    
    

        # clear_times_list=times_list.copy()
        # for i in range(len(clear_times_list)):
        #     if clear_times_list[i]==0:
        #         continue
        #     else:
        #         for j in range(i+1,len(clear_times_list)):
        #             if clear_times_list[i]==clear_times_list[j]:
        #                 clear_times_list[j]=0
        # i,j=0,0
        # '''清楚重复元素''
        # for i in range(len(clear_times_list)):
        #     if clear_times_list[i]==0:
        #         continue
        #     else:
        #         cleaned_times_list.append(clear_times_list[i])
        # '''收集有效数据并添加到cleaned_times_list中'''
    '''清楚重复元素，不能保证重复的元素都没意义，所以不能用这种方法'''
                  

                



