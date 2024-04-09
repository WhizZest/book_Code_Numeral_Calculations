import numpy as np
import matplotlib.pyplot as plt

# 给定数据
xi = np.array([1.00, 1.25, 1.50, 1.75, 2.00])
yi = np.array([5.10, 5.79, 6.53, 7.45, 8.46])

# 将模型转化为线性形式：ln(y) = ln(a) + b * x
ln_yi = np.log(yi)

# 使用最小二乘法拟合线性模型
coefficients = np.polyfit(xi, ln_yi, 1)

# 拟合得到的参数
b_fit, ln_a_fit = coefficients

# 计算参数 a
a_fit = np.exp(ln_a_fit)

# 输出拟合参数
print("Parameters: a =", a_fit, ", b =", b_fit)

# 构建拟合函数
def model_function(x, a, b):
    return a * np.exp(b * x)

# 生成拟合曲线上的点
x_values = np.linspace(np.min(xi), np.max(xi), 100)
y_values = model_function(x_values, a_fit, b_fit)

# 绘制数据散点图和拟合曲线
plt.scatter(xi, yi, label='Data Points')
plt.plot(x_values, y_values, color='red', label='Exponential Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Fit of the given data')
plt.legend()
plt.show()