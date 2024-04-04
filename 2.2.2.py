import numpy as np

def cholesky_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i+1):
            if i == j:
                L[i, j] = np.sqrt(A[i, j] - np.sum(L[i, :j]**2))
            else:
                L[i, j] = (A[i, j] - np.dot(L[i, :j], L[j, :j])) / L[j, j]
    return L

def solve_cholesky(L, b):
    # Ly = b
    y = np.linalg.solve(L, b)
    # L^T x = y
    x = np.linalg.solve(L.T, y)
    return x

# 定义矩阵 A 和向量 b
A = np.array([[4, 2, -2],
              [2, 2, -3],
              [-2, -3, 14]])
b = np.array([4, 1, 0]).reshape(-1, 1)  # 确保 b 是列向量 

# 进行 Cholesky 分解
L = cholesky_decomposition(A)

# 求解方程组
x = solve_cholesky(L, b)

print("L 矩阵:")
print(L)
print("\n方程组的解 x:")
print(x)
