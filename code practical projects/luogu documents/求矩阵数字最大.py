'''def create_matrix_from_input():
    # 用户输入矩阵的行数和列数
    m = int(input("请输入矩阵的行数: "))
    n = int(input("请输入矩阵的列数: "))

    # 用户输入矩阵的元素
    print("请输入矩阵的元素，每个数字之间用空格分隔:")
    elements = list(map(int, input().split()))

    # 检查输入的元素数量是否正确
    if len(elements) != m * n:
        raise ValueError("输入的元素数量与矩阵的维度不匹配")

    # 将一维列表转换为二维矩阵
    matrix = [elements[i * n:(i + 1) * n] for i in range(m)]

    return matrix

# 生成矩阵并打印
matrix = create_matrix_from_input()
for row in matrix:
    print(row)
print(matrix)'''












matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 使用列表推导式展平矩阵
flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 找出最大值
x=0
for i in range(len(flattened_matrix)):
    if x<=flattened_matrix[i]:
        x=flattened_matrix[i]
    else :
        continue
print(x)




for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if x<=matrix[i][j]:
            x=matrix[i][j]
        else :
            continue
print(x)
    