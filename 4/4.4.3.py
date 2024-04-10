import numpy as np
import matplotlib.pyplot as plt

# 给定数据
xi = np.array([0, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
yi = np.array([1, 1.75, 1.96, 2.19, 2.44, 2.71, 3.00])
wi = np.array([1, 1, 1, 1, 1, 1, 1])  # 权系数

# 最小二乘拟合二次多项式
coefficients = np.polyfit(xi, yi, 2, w=wi)

# 输出拟合多项式的系数
print("Coefficients of the quadratic fit:", coefficients)

# 构建拟合函数
p = np.poly1d(coefficients)

# 生成拟合曲线上的点
x_values = np.linspace(np.min(xi), np.max(xi), 100)
y_values = p(x_values)

# 绘制数据散点图和拟合曲线
plt.scatter(xi, yi, label='Data Points')
plt.plot(x_values, y_values, color='red', label='Quadratic Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Fit of the given data with weights')
plt.legend()
plt.show()