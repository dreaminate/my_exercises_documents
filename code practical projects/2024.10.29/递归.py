

def factorial(n) :
    if n < 0:
        print("没有定义负数的阶乘")
        
    if n == 0:
        return 1
    else:
        return n *factorial(n-1)
n=int(input())
print("n! = ",factorial(n))


