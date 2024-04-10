import numpy as np
import matplotlib.pyplot as plt

# 给定数据
xi = np.array([0, 0.25, 0.50, 0.75, 1.00])
yi = np.array([1.0000, 1.2840, 1.6487, 2.1170, 2.7183])

# 最小二乘拟合二次多项式
coefficients = np.polyfit(xi, yi, 2)

# 构建拟合函数
p = np.poly1d(coefficients)
print("Fit function:", p)

# 生成拟合曲线上的点
x_values = np.linspace(np.min(xi), np.max(xi), 100)
y_values = p(x_values)

# 输出拟合多项式的系数
print("Coefficients of the quadratic fit:", coefficients)

# 绘制数据散点图和拟合曲线
plt.scatter(xi, yi, label='Data Points')
plt.plot(x_values, y_values, color='red', label='Quadratic Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Fit of the given data')
plt.legend()
plt.show()