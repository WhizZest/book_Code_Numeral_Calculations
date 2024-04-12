import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if x == 0:
        return 1  # 处理在 x = 0 处的除零情况
    else:
        return np.sin(x) / x

def monte_carlo_integration(f, x_range, num_samples):
    x_min, x_max = x_range
    
    x_samples = np.random.uniform(x_min, x_max, num_samples)
    
    integral_sum = 0
    for i in range(num_samples):
        integral_sum += f(x_samples[i])
    
    # 计算积分的平均值
    integral = (x_max - x_min) * (integral_sum / num_samples)
    return integral

# 定义积分范围和采样数量
x_range = (0, 2)
num_samples_list = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]

# 存储积分值和误差
integral_values = []
errors = []

# 计算真实值
# sin(x)/x 在给定范围内的解析积分没有简单的闭式表达式，因此我们将使用数值积分作为真实值的近似
true_integral = np.trapz([f(x) for x in np.linspace(0, 2, 10000)], np.linspace(0, 2, 10000))

# 对不同的采样数量进行循环计算
for num_samples in num_samples_list:
    estimated_integral = monte_carlo_integration(f, x_range, num_samples)
    integral_values.append(estimated_integral)
    errors.append(abs(true_integral - estimated_integral))

# 打印真实值
print("True Integral:", true_integral)
# 打印蒙特卡罗积分值
print("Estimated Integral Values:", integral_values)
# 打印误差
print("Errors:", errors)

# 绘制两张图像
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# 左图：积分值随采样数量的变化
axs[0].plot(num_samples_list, integral_values, marker='o')
axs[0].set_xscale('log')
axs[0].set_xlabel('Number of Samples')
axs[0].set_ylabel('Estimated Integral Value')
axs[0].set_title('Monte Carlo Integration Value vs. Number of Samples')
axs[0].grid(True)

# 右图：误差随采样数量的变化
axs[1].plot(num_samples_list, errors, marker='o')
axs[1].set_xscale('log')
axs[1].set_yscale('log')
axs[1].set_xlabel('Number of Samples')
axs[1].set_ylabel('Error')
axs[1].set_title('Error of Monte Carlo Integration vs. Number of Samples')
axs[1].grid(True)

plt.tight_layout()
plt.show()
