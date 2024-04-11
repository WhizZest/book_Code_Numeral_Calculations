import numpy as np
import matplotlib.pyplot as plt
from scipy.special import roots_hermite
from scipy.integrate import quad

def f_gauss(x):
    return np.cos(x)

def f_quad(x):
    return np.exp(-x ** 2) * np.cos(x)

def gauss_hermite_integral(n, func):
    # 获取高斯–埃尔米特节点和权重
    x, w = roots_hermite(n)
    
    # 计算积分值的近似值
    approx_integral = np.sum(w * func(x))
    
    return approx_integral

# 计算不同阶数下的积分结果和误差
max_n = 15
integral_results = []
errors = []

for n in range(1, max_n + 1):
    integral = gauss_hermite_integral(n, f_gauss)
    actual_integral, _ = quad(f_quad, -np.inf, np.inf)
    error = np.abs(integral - actual_integral)
    integral_results.append(integral)
    errors.append(error)

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘制积分结果随阶数变化的图像
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(range(1, max_n + 1), integral_results, marker='o')
plt.xlabel('阶数 $n$')
plt.ylabel('积分结果')
plt.title('高斯–埃尔米特积分结果随阶数变化')

# 绘制误差随阶数变化的图像
plt.subplot(1, 2, 2)
plt.plot(range(1, max_n + 1), errors, marker='o', color='orange')
plt.xlabel('阶数 $n$')
plt.ylabel('In(误差)')
plt.title('误差随阶数变化')
plt.yscale('log')

plt.tight_layout()
plt.show()
