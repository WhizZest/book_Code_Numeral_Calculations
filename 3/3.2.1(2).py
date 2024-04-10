import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# 已知点
x_known = np.array([10, 11, 12, 13, 14])
y_known = np.array([2.3026, 2.3979, 2.4849, 2.5649, 2.6391])

# 使用拉格朗日插值计算多项式（拉格朗日插值）
poly = lagrange(x_known, y_known)

# 定义ln函数
def ln_function(x):
    return np.log(x)

# 计算ln函数在相同的x值上的值
x_values = np.linspace(1, 25, 200)
y_ln = ln_function(x_values)

# 计算线性插值
x_known_linear = [11, 12]
y_known_linear = [2.3979, 2.4849]
poly_linear = lagrange(x_known_linear, y_known_linear)
y_linear = poly_linear(x_values)

# 计算抛物线插值
x_known_parabolic = [11, 12, 13]
y_known_parabolic = [2.3979, 2.4849, 2.5649]
poly_parabolic = lagrange(x_known_parabolic, y_known_parabolic)
y_parabolic = poly_parabolic(x_values)

# 绘图
plt.plot(x_values, y_ln, label='ln(x)')
plt.plot(x_values, y_linear, label='Linear Interpolation')
plt.plot(x_values, y_parabolic, label='Parabolic Interpolation')
plt.plot(x_values, poly(x_values), label='Lagrange Interpolation')
plt.scatter(x_known, y_known, color='red', label='Known Points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Interpolation Methods')
plt.legend()
plt.grid(True)
plt.show()
