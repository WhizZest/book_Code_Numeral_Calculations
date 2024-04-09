import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 定义模型函数
def model_function(x, a, b, c):
    return a * np.log(x) + b * np.cos(x) + c * np.exp(x)

# 给定数据
xi = np.array([0.24, 0.65, 0.95, 1.24, 1.73, 2.01, 2.23, 2.52, 2.77, 2.99])
yi = np.array([0.23, -0.26, -1.10, -0.45, 0.27, 0.10, -0.29, 0.24, 0.56, 1.00])

# 使用最小二乘法拟合数据
popt, pcov = curve_fit(model_function, xi, yi)

# 拟合得到的参数
a_fit, b_fit, c_fit = popt

# 生成拟合曲线上的点
x_values = np.linspace(np.min(xi), np.max(xi), 100)
y_values = model_function(x_values, a_fit, b_fit, c_fit)

# 输出拟合参数
print("Parameters: a =", a_fit, ", b =", b_fit, ", c =", c_fit)

# 绘制数据散点图和拟合曲线
plt.scatter(xi, yi, label='Data Points')
plt.plot(x_values, y_values, color='red', label='Fitted Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve Fit of the given data')
plt.legend()
plt.show()