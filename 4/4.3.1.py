import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 定义原函数 f(x)
def f(x):
    return np.sqrt(1 + x**2)

# 定义线性模型 p1(x) = a0 + a1*x
def p1(x, a0, a1):
    return a0 + a1 * x

# 生成数据点
x_data = np.linspace(0, 1, 1000)
y_data = f(x_data)

# 使用 curve_fit 进行拟合
params, covariance = curve_fit(p1, x_data, y_data)

# 得到拟合系数
a0, a1 = params

# 打印拟合系数
print("拟合系数:")
print("a0 =", a0)
print("a1 =", a1)

# 绘图
plt.plot(x_data, y_data, label='Original Function: $f(x) = \sqrt{1+x^2}$')
plt.plot(x_data, p1(x_data, a0, a1), label='Linear Approximation: $p_1(x) = %.2f + %.2f x$' % (a0, a1))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Original Function and Linear Approximation')
plt.legend()
plt.grid(True)
plt.show()
