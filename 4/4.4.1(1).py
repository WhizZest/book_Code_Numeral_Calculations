import numpy as np  
from scipy.optimize import curve_fit  
import matplotlib.pyplot as plt  
  
# 给定的数据  
xi = np.array([0.24, 0.65, 0.95, 1.24, 1.73, 2.01, 2.23, 2.52, 2.77, 2.99])  
yi = np.array([0.23, -0.26, -1.10, -0.45, 0.27, 0.10, -0.29, 0.24, 0.56, 1.00])  
  
# 定义模型函数  
def model(x, a, b, c):  
    return a * np.log(x) + b * np.cos(x) + c * np.exp(x)  
  
# 使用 curve_fit 进行拟合  
params, covariance = curve_fit(model, xi, yi)  
  
# 输出拟合参数  
print("拟合参数: a = {}, b = {}, c = {}".format(params[0], params[1], params[2]))  
  
# 绘制原始数据和拟合曲线  
x_fit = np.linspace(min(xi), max(xi), 100)  
y_fit = model(x_fit, *params)  

plt.rcParams['font.family'] = 'SimHei'  # 设置字体为 SimHei，适用于 Windows  
# 或者在 macOS 和 Linux 上使用 'WenQuanYi Zen Hei' 或其他支持中文的字体  
plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题 
  
plt.scatter(xi, yi, label='原始数据')  
plt.plot(x_fit, y_fit, color='red', label='拟合曲线')  
plt.legend()  
plt.show()