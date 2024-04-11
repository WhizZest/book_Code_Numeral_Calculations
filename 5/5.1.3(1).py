import numpy as np
from scipy.integrate import trapz, simps

# 定义函数
def f(x):
    return np.sin(x) / x

# 定义积分区间和节点
a = 0  # 下限
b = 1  # 上限
x_nodes = np.array([0, 1/8, 1/4, 3/8, 1/2, 5/8, 3/4, 7/8, 1])  # 节点
y_values = np.array([1, 0.9973978, 0.9896158, 0.9767267, 0.9538510, 0.9351556, 0.9088516, 0.8771925, 0.8424709])  # 函数值

# 使用复合梯形公式计算积分
integral_trapezoidal = trapz(y_values, x_nodes)

# 使用复合辛普森公式计算积分
integral_simpson = simps(y_values, x_nodes)

print("复合梯形公式计算的积分值:", integral_trapezoidal)
print("复合辛普森公式计算的积分值:", integral_simpson)
