import numpy as np

# 定义函数
def f(x):
    return np.sin(x) / x

# 复合梯形公式
def composite_trapezoidal_rule(x, y):
    n = len(x) - 1
    h = (x[-1] - x[0]) / n
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])
    return integral

# 复合辛普森公式
def composite_simpson_rule(x, y):
    n = len(x) - 1
    h = (x[-1] - x[0]) * 2 / n
    integral = h / 6 * (y[0] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]) + y[n])
    return integral

# 给定数据点
x = np.array([0, 1/8, 1/4, 3/8, 1/2, 5/8, 3/4, 7/8, 1])
y = np.array([1, 0.9973978, 0.9896158, 0.9767267, 0.9538510, 0.9351556, 0.9088516, 0.8771925, 0.8424709])

# 使用复合梯形公式计算积分
integral_trapezoidal = composite_trapezoidal_rule(x, y)
print("复合梯形公式计算的积分值:", integral_trapezoidal)

# 使用复合辛普森公式计算积分
integral_simpson = composite_simpson_rule(x, y)
print("复合辛普森公式计算的积分值:", integral_simpson)
