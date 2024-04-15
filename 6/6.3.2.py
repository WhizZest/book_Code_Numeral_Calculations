import numpy as np  
from scipy.sparse.linalg import gmres  
  
# 定义系数矩阵A和向量b  
A = np.array([[4, -1.2, 0], [-0.8, 4, -1.2], [0, -0.8, 4]])  
b = np.array([2.8, 2, 3.2])  
  
# 使用GMRES方法求解Ax=b  
x, exitCode = gmres(A, b)  
  
# 打印解向量x  
print("解向量x:")  
print(x)  
  
# 验证解的正确性（可选）  
residual = np.linalg.norm(A.dot(x) - b)  
print("残差范数:", residual)