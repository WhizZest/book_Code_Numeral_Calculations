import numpy as np  
from scipy.special import roots_laguerre  
from scipy.integrate import quad  
import matplotlib.pyplot as plt  
  
# 原始函数  
def f(x):  
    return 1 / (1 + x**3)  
  
# 使用高斯-拉盖尔公式计算积分  
def gauss_laguerre_integration(n, a=2):  
    x, w = roots_laguerre(n)  # 获取拉盖尔多项式的根和权重  
    integral = sum(w[i] * f(x[i] + a) * np.exp(x[i]) for i in range(n))  
    return integral  
  
# 计算实际积分值  
actual_integral, _ = quad(f, 2, np.inf)  
  
# 准备数据点  
n_values = np.arange(2, 21)  # 从2到50的点数  
approx_integrals = []  
errors = []  
  
# 计算每个n值的高斯-拉盖尔积分和误差  
for n in n_values:  
    approx_integral = gauss_laguerre_integration(n)  
    approx_integrals.append(approx_integral)  
    errors.append(abs(approx_integral - actual_integral))  
  
# 绘制高斯-拉盖尔积分结果  
plt.figure(figsize=(12, 6))  
  
plt.subplot(1, 2, 1)  # 第一个子图  
plt.plot(n_values, approx_integrals, 'o-', label='Gauss-Laguerre Integral')  
plt.axhline(y=actual_integral, color='r', linestyle='--', label='Actual Integral')  
plt.xlabel('Number of points (n)')  
plt.ylabel('Integral Value')  
plt.title('Gauss-Laguerre Integration Results')  
plt.legend()  
  
# 绘制误差图像  
plt.subplot(1, 2, 2)  # 第二个子图  
plt.plot(n_values, errors, 'o-')  
plt.xlabel('Number of points (n)')  
plt.ylabel('Error')  
plt.title('Error of Gauss-Laguerre Integration')  
#plt.yscale('log')  # 使用对数刻度，以便更好地展示误差的变化  
  
# 显示图像  
plt.tight_layout()  
plt.show()