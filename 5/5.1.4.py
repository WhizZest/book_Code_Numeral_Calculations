import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from tabulate import tabulate

# 定义函数
def f(x):
    return x * np.exp(-x) * np.cos(2 * x)

# 精确积分值
exact_integral = (3*(np.exp(-2*np.pi)-1) - 10*np.pi*np.exp(-2*np.pi)) / 25

# 积分区间
a = 0
b = 2 * np.pi

# 计算不同数量的子区间下的积分值
num_subintervals = [2**k for k in range(9)]

integral_midpoint = []
integral_trapezoidal = []
integral_simpson = []

error_midpoint = []
error_trapezoidal = []
error_simpson = []

for n in num_subintervals:
    h = (b - a) / n
    x_midpoints = np.linspace(a + h / 2, b - h / 2, n)
    integral_midpoint.append(h * np.sum(f(x_midpoints)))
    error_midpoint.append(np.abs(integral_midpoint[-1] - exact_integral))
    
    x_trapezoidal = np.linspace(a, b, n+1)
    integral_trapezoidal.append(h / 2 * (f(a) + 2 * np.sum(f(x_trapezoidal[1:-1])) + f(b)))
    error_trapezoidal.append(np.abs(integral_trapezoidal[-1] - exact_integral))
    
    x_simpson = np.linspace(a, b, 2*n+1)
    integral_simpson.append(h / 6 * (f(a) + 4 * np.sum(f(x_simpson[1::2])) + 2 * np.sum(f(x_simpson[2:-1:2])) + f(b)))
    error_simpson.append(np.abs(integral_simpson[-1] - exact_integral))

# 创建结果表格
table = [["Number of Subintervals", "Midpoint", "Trapezoidal", "Simpson"],
         ["Exact Integral", exact_integral, exact_integral, exact_integral]]

for i, n in enumerate(num_subintervals):
    table.append([n, integral_midpoint[i], integral_trapezoidal[i], integral_simpson[i]])

# 打印表格
print(tabulate(table, headers="firstrow", floatfmt=".10f", stralign="right"))

# 打印误差表格
error_table = [["Number of Subintervals", "Midpoint Error", "Trapezoidal Error", "Simpson Error"]]
for i in range(len(num_subintervals)):
    error_table.append([num_subintervals[i], error_midpoint[i], error_trapezoidal[i], error_simpson[i]])

print(tabulate(error_table, headers="firstrow", floatfmt=(".0e", ".3e", ".3e", ".3e")))

num_subintervals_log10 = np.log10(num_subintervals)
# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(num_subintervals_log10, np.log10(error_midpoint), label='Midpoint', marker='o')
plt.plot(num_subintervals_log10, np.log10(error_trapezoidal), label='Trapezoidal', marker='o')
plt.plot(num_subintervals_log10, np.log10(error_simpson), label='Simpson', marker='o')

plt.title('Convergence of Numerical Integration Methods')
plt.xlabel('Number of Subintervals')
plt.ylabel('Absolute Error')
#plt.xscale('log')
#plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show()
