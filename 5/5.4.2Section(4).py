import numpy as np  
from scipy.special import roots_hermite  
  
# 指定高斯点的数量  
n = 5  
  
# 使用 scipy 函数计算高斯点和权重  
# 注意：roots_hermite 返回的高斯点是标准化后的，即对应于权重函数 e^(-x^2/2)  
x, w = roots_hermite(n)   
  
# 打印高斯点和权重  
print("高斯点：")  
print(x)  
print("高斯系数：")  
print(w)