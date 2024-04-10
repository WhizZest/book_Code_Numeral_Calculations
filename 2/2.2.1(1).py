import numpy as np  
from scipy.linalg import lu_factor, lu_solve  
  
# 定义矩阵A和向量b  
A = np.array([[1, 2, 3, 4],  
              [1, 4, 9, 16],  
              [1, 8, 27, 64],  
              [1, 16, 81, 256]], dtype=float)  
  
b = np.array([2, 10, 44, 190], dtype=float).reshape(-1, 1)  
  
# 进行LU分解  
lu, piv = lu_factor(A)  
  
# 从LU分解中提取L和U  
L = np.tril(lu, k=-1) + np.identity(lu.shape[0])  
U = np.triu(lu)  
  
# 修正L中的行置换（如果需要）  
for i, p in enumerate(piv):  
    L[i, :] = L[i, :][piv]  
    L[:, i] = L[:, p]  
    L[i, i] = 1  # 保证对角线上是1  
  
# 打印L和U  
print("L (下三角矩阵):")  
print(L)  
print("U (上三角矩阵):")  
print(U)  
  
# 使用LU分解解方程组Ax=b  
x = lu_solve((lu, piv), b)  
  
# 打印解向量x  
print("解向量x:")  
print(x)