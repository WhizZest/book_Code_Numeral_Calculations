import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 定义拟合函数形式
def func(x, a, b):
    return a * np.sin(np.pi * x) + b * np.cos(np.pi * x)

# 给定数据点
x_data = np.array([-1, -1/2, 0, 1/2, 1])
y_data = np.array([-1, 0, 1, 2, 1])

# 使用 curve_fit 进行拟合
popt, pcov = curve_fit(func, x_data, y_data)

# 获取拟合参数
a_fit, b_fit = popt

print("拟合参数 a:", a_fit)
print("拟合参数 b:", b_fit)

# 绘制原始数据和拟合曲线
x_fit = np.linspace(-1, 1, 100)
y_fit = func(x_fit, a_fit, b_fit)

plt.scatter(x_data, y_data, label='Original Data')
plt.plot(x_fit, y_fit, 'r', label='Fitted Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Curve Fitting')
plt.grid(True)
plt.show()
