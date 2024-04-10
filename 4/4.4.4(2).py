import numpy as np  
from scipy import stats  
import matplotlib.pyplot as plt  
  
# 给定数据  
xi = np.array([1.00, 1.25, 1.50, 1.75, 2.00])  
yi = np.array([5.10, 5.79, 6.53, 7.45, 8.46])  
  
# 对数变换  
Yi = np.log(yi)  
  
# 使用线性最小二乘法拟合变换后的数据  
slope, intercept, r_value, p_value, std_err = stats.linregress(xi, Yi)  
  
# 恢复原始模型中的参数 a  
a = np.exp(intercept)  
b = slope  
  
# 输出拟合参数  
print("拟合参数: a = {:.4f}, b = {:.4f}".format(a, b))  
  
# 绘制原始数据和拟合曲线  
x_fit = np.linspace(min(xi), max(xi), 100)  
y_fit = a * np.exp(b * x_fit)  

plt.rcParams['font.family'] = 'SimHei'  # 设置字体为 SimHei，适用于 Windows  
# 或者在 macOS 和 Linux 上使用 'WenQuanYi Zen Hei' 或其他支持中文的字体  
plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题 

plt.scatter(xi, yi, label='原始数据')  
plt.plot(x_fit, y_fit, color='red', label='拟合曲线')  
plt.legend()  
plt.xlabel('x')  
plt.ylabel('y')  
plt.show()