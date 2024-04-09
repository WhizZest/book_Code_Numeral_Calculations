import numpy as np  
from scipy.optimize import least_squares  
import matplotlib.pyplot as plt  
  
# 给定的数据点  
x_data = np.array([-1, -1/2, 0, 1/2, 1])  
y_data = np.array([-1, 0, 1, 2, 1])  
  
# 定义构建三角多项式基函数的函数  
def build_trigonometric_basis(order):  
    def trigonometric_polynomial(x, *coeffs):  
        total = coeffs[0]  # a0 coefficient  
        for i in range(1, order + 1):  
            total += coeffs[2 * i - 1] * np.cos(i * np.pi * x) + coeffs[2 * i] * np.sin(i * np.pi * x)  
        return total  
    return trigonometric_polynomial  
  
# 定义残差函数，用于least_squares方法  
def residuals(coeffs, x, y, trig_poly):  
    return trig_poly(x, *coeffs) - y  
  
# 设置三角多项式的阶数  
order = 3  # 你可以修改这个值来改变三角多项式的阶数  
  
# 构建对应阶数的三角多项式函数  
trig_poly = build_trigonometric_basis(order)  
  
# 初始系数猜测，长度为2*order + 1（a0, a1, b1, a2, b2, ..., an, bn）  
initial_guess = np.zeros(2 * order + 1)  
  
# 使用least_squares方法进行拟合  
result = least_squares(residuals, initial_guess, args=(x_data, y_data, trig_poly))  
  
# 输出拟合结果  
print("拟合系数:", result.x)  
  
# 使用拟合的系数绘制拟合曲线  
x_fit = np.linspace(-1.5, 1.5, 100)  
y_fit = trig_poly(x_fit, *result.x)  

plt.rcParams['font.family'] = 'SimHei'  # 设置字体为 SimHei，适用于 Windows  
# 或者在 macOS 和 Linux 上使用 'WenQuanYi Zen Hei' 或其他支持中文的字体  
plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题

plt.scatter(x_data, y_data, label='数据点')  
plt.plot(x_fit, y_fit, 'r-', label='拟合曲线')  
plt.legend()  
plt.xlabel('x')  
plt.ylabel('y')  
plt.title(f'三角多项式拟合（阶数：{order}）')  
plt.grid(True)  
plt.show()