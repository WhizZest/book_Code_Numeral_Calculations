import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 定义节点和函数值
x_nodes = np.array([0, 1, 2, 3])
y_values = np.array([0, 0.5, 2.0, 1.5])

# 定义一阶导数值
y_prime_values = np.array([0.2, None, None, -1])

# 使用CubicSpline类计算三次样条插值函数
spline = CubicSpline(x_nodes, y_values, bc_type=((1, y_prime_values[0]), (1, y_prime_values[-1])))

# 获取分段函数的系数
coefficients = spline.c

# 打印系数
#print("Coefficients:\n", coefficients.T)
for i, coef in enumerate(coefficients.T):
    print(f"Segment {i+1} coefficients (a, b, c, d): {coef}")

# 绘制样条插值函数图像
x_values = np.linspace(0, 3, 100)
plt.plot(x_values, spline(x_values), label='Cubic Spline Interpolation')
plt.scatter(x_nodes, y_values, color='red', label='Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic Spline Interpolation')
plt.legend()
plt.grid(True)
plt.show()
