import numpy as np

def doolittle_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        U[j, j:] = A[j, j:] - L[j, :j] @ U[:j, j:]
        L[j:, j] = (A[j:, j] - L[j:, :j] @ U[:j, j]) / U[j, j]

    return L, U

def solve_doolittle(L, U, b):
    # Ly = b
    y = np.linalg.solve(L, b)
    # Ux = y
    x = np.linalg.solve(U, y)
    return x

# 定义矩阵 A 和向量 b
A = np.array([[1, 2, 3, 4],
              [1, 4, 9, 16],
              [1, 8, 27, 64],
              [1, 16, 81, 256]])
b = np.array([2, 10, 44, 190])

# 进行杜利脱尔分解
L, U = doolittle_decomposition(A)

# 求解方程组
x = solve_doolittle(L, U, b)

print("L 矩阵:")
print(L)
print("\nU 矩阵:")
print(U)
print("\n方程组的解 x:")
print(x)
