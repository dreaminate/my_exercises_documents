import random
def division(num1,num2):
    return (num1+num2)/2
    ''' 两个数相加再除2'''

random_maxium = int(input("Enter the maxium number of the range: "))
right_num = random.randint(1,random_maxium)
guess_num = random.randint(1,random_maxium)
print(f"{right_num} is the right number.",end="\n\n")
# print(guess_num)
lower_num=1
higher_num=random_maxium
guess_count=0
times_list=[]
while len(times_list)<=1000:
    while True:
        if guess_num > right_num:
            print(f"This is my {guess_count}time,i guess {guess_num} is too high.",end="\n\n")
            higher_num = guess_num
            guess_num =division(guess_num,lower_num)
            guess_count+=1
            # print(guess_num)
        elif guess_num < right_num:
            print(f"This is my {guess_count}time,i guess {guess_num} is too low.",end="\n\n")
            lower_num = guess_num
            guess_num =division(guess_num,higher_num)
            guess_count+=1
            # print(guess_num)
        else:
            print(f"This is my {guess_count}time,i guess {guess_num} is right.")
            times_list.append(guess_count)
            guess_num = random.randint(1,random_maxium)
            guess_count=0
            break
prediction_times=sum(times_list)/len(times_list)
print(f"Average prediction times is {prediction_times}.\nAnd the mached num is {random_maxium}.")
'''还想尝试一下，上限与prediction_times的关系，看看是否有规律。'''