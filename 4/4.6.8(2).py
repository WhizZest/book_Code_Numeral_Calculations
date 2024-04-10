import numpy as np  
from scipy.optimize import curve_fit  
import matplotlib.pyplot as plt  
  
# 给定的数据点  
x_data = np.array([-1, -1/2, 0, 1/2, 1])  
y_data = np.array([-1, 0, 1, 2, 1])  
  
# 定义三角多项式函数  
def trigonometric_polynomial(x, *coeffs):  
    """任意阶三角多项式函数"""  
    total = coeffs[0]  # 第一个系数是a0  
    n_coeffs = len(coeffs)  
    order = (n_coeffs - 1) // 2  # 根据系数数量计算多项式的阶数  
    for i in range(1, order + 1):  
        a_coeff = coeffs[2 * i - 1]  
        b_coeff = coeffs[2 * i] if 2 * i < n_coeffs else 0  
        total += a_coeff * np.cos(i * np.pi * x) + b_coeff * np.sin(i * np.pi * x)  
    return total
  
# 设置三角多项式的阶数和初始系数  
polynomial_order = 1  # 例如，3阶三角多项式  
num_coeffs = 2 * polynomial_order + 1  # 根据阶数计算系数数量  
initial_guess = np.zeros(num_coeffs)  # 创建与系数数量相等的初始猜测数组  
  
# 确保有足够的数据点  
assert len(x_data) >= num_coeffs, "数据点数量必须大于或等于系数数量"  
  
# 使用curve_fit进行拟合  
coeffs, _ = curve_fit(trigonometric_polynomial, x_data, y_data, p0=initial_guess)  
  
# 输出拟合得到的系数  
print("拟合系数:", coeffs)
  
# 使用拟合的系数绘制拟合曲线  
x_fit = np.linspace(-1, 1, 100)  
y_fit = trigonometric_polynomial(x_fit, *coeffs)  

plt.rcParams['font.family'] = 'SimHei'  # 设置字体为 SimHei，适用于 Windows  
# 或者在 macOS 和 Linux 上使用 'WenQuanYi Zen Hei' 或其他支持中文的字体  
plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题

plt.scatter(x_data, y_data, label='数据点')  
plt.plot(x_fit, y_fit, 'r-', label='拟合曲线')  
plt.legend()  
plt.xlabel('x')  
plt.ylabel('y')  
plt.title('三角多项式拟合')  
plt.grid(True)  
plt.show()