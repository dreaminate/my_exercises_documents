def decompose(n):
    bits = []
    while n:
        bits.append(n % 2)
        n = n // 2
    flag = 0    # 这个flag用来判断是不是第一项

    for i in range(len(bits) - 1, 1, -1): # 从最高项到2位，1位和0位特殊处理
        if bits[i]:
            if flag:
                print('+', end='')
            else:
                flag = 1
            print("2(", end='')
            decompose(i)
            print(")", end='')

    if bits[1]:
        if flag:
            print("+2", end='')
        else:
            print("2", end='')
            flag = 1
    if bits[0]:
        if flag:
            print("+2(0)", end='')
        else:
            print("2(0)", end='')
            flag = 1

n = int(input())
decompose(n)
print("")