import numpy as np  
  
# 定义矩阵 A 和向量 b  
A = np.array([[4, 2, -2],  
              [2, 2, -3],  
              [-2, -3, 14]], dtype=float)  
b = np.array([4, 1, 0], dtype=float).reshape(-1, 1)  # 确保 b 是列向量  
  
# 执行 Cholesky 分解  
L = np.linalg.cholesky(A)  
  
# 使用前向代入法求解 L * y = b  
y = np.linalg.solve(L, b)  
  
# 使用后向代入法求解 L^T * x = y  
x = np.linalg.solve(L.T, y)  
  
print("矩阵 L:")  
print(L)  
print("\n解向量 x:")  
print(x)