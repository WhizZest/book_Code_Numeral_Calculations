import numpy as np

def thomas_algorithm(A, d):
    n = len(d)
    
    # 初始化 u, y 向量
    u = np.zeros(n-1)
    y = np.zeros(n)
    
    # 计算 u, y 向量
    u[0] = A[0, 1] / A[0, 0]
    y[0] = d[0] / A[0, 0]
    for i in range(1, n-1):
        u[i] = A[i, i+1] / (A[i, i] - A[i, i-1] * u[i-1])
        y[i] = (d[i] - A[i, i-1] * y[i-1]) / (A[i, i] - A[i, i-1] * u[i-1])
    # 最后一个元素单独处理
    y[n-1] = (d[n-1] - A[n-1, n-2] * y[n-2]) / (A[n-1, n-1] - A[n-1, n-2] * u[n-2])
    
    # 回代求解 x 向量
    x = np.zeros(n)
    x[-1] = y[-1]
    for i in range(n-2, -1, -1):
        x[i] = y[i] - u[i] * x[i+1]
    
    return x

# 定义矩阵 A 和向量 d
A = np.array([[2, -1, 0, 0],
              [-1, 3, -2, 0],
              [0, -2, 4, -3],
              [0, 0, -3, 5]])
d = np.array([6, 1, -2, 1])

# 使用追赶法求解方程组
x = thomas_algorithm(A, d)

print("方程组的解 x:")
print(x)
