import numpy as np  
import matplotlib.pyplot as plt  
from scipy.optimize import minimize  
  
# 定义目标函数 f(x) = sqrt(x)  
def f(x):  
    return np.sqrt(x)  
  
# 定义逼近多项式 p(x) = ax + b  
def p(x, a, b):  
    return a * x + b  
  
# 定义平方误差函数  
def square_error(coeffs, x_values):  
    a, b = coeffs  
    return np.sum((f(x_values) - p(x_values, a, b)) ** 2)  
  
# 在 [0, 1] 区间内均匀采样一些点  
x_values = np.linspace(0, 1, 1000)  
  
# 使用 scipy 的 minimize 函数来找到最佳逼近多项式的系数  
initial_guess = [1, 1]  # 初始猜测值 for a and b  
result = minimize(square_error, initial_guess, args=(x_values,))  
a, b = result.x  
  
# 打印最佳系数  
print(f"Best coefficients: a = {a}, b = {b}")  
  
# 绘制对比图像  
plt.figure(figsize=(10, 6))  
plt.plot(x_values, f(x_values), label=r'$f(x) = \sqrt{x}$')  
plt.plot(x_values, p(x_values, a, b), label=r'$p(x) = ax + b$', linestyle='--')  
plt.xlabel('x')  
plt.ylabel('y')  
plt.title('Best Square Approximation of sqrt(x) on [0, 1]')  
plt.legend()  
plt.grid(True)  
plt.show()