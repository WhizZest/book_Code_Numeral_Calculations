import numpy as np

A = np.array([[2, 3],
              [1, -4],
              [2, -1]])

b = np.array([1, -9, -1])

# 使用最小二乘法求解
x_hat = np.linalg.lstsq(A, b, rcond=None)[0]

print("最佳近似解为:", x_hat)
