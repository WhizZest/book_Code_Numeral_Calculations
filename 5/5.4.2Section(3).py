import numpy as np  
from scipy.special import roots_laguerre  
  
# 指定高斯点的数量  
n = 5  
  
# 使用 scipy 函数计算高斯点和权重  
x, w = roots_laguerre(n)  
  
# 打印高斯点和权重  
print("高斯点：")  
print(x)  
print("高斯系数：")  
print(w)