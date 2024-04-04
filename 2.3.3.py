import numpy as np  
  
# 给定向量x
x = np.array([2, 1, 1]).reshape(-1, 1)  
print("x向量:", x)
  
# 计算反射向量u  
norm_x = np.linalg.norm(x) # 计算向量x的模 
print("向量x的模:", norm_x)
sign_x1 = np.sign(x[0])  # 计算a的符号
k = -sign_x1*norm_x
print("k:", k)
y = k*np.array([1, 0, 0]).reshape(-1, 1)
print("y=ke:", y)
u = x + sign_x1 * norm_x * np.array([1, 0, 0]).reshape(-1, 1)  
print("反射向量u:", u)
  
# 计算Householder矩阵P1  
P1 = np.eye(3) - 2 * np.dot(u, u.T) / np.dot(u.T, u)  
  
print("P1矩阵:")  
print(P1)  
  
# 验证P1 * x = y  
result = np.dot(P1, x)  
print("\nP1 * x 结果:")  
print(result)