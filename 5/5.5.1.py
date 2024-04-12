import numpy as np
from scipy.integrate import dblquad
from math import sin, pi

# 定义给定的函数
def f(x, y):
    return np.sin(x + y)

# 定义复合辛普森规则
def composite_simpson(f, a, b, m):
    h = (b - a) / m
    x = np.linspace(a, b, m+1)
    y = np.array([f(xi) for xi in x])
    #print("y:", y)
    #print("len(y):", len(y))
    #integral = h / 3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])#如果y的长度为奇数，这样算会遗漏掉y[-1]
    integral = h / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]))
    return integral

# 定义 x 和 y 的范围
x_min, x_max = 0, np.pi/2
y_min, y_max = 0, np.pi/4

# 定义分割数
m = 4

# 计算二重积分的实际值
actual_value, error = dblquad(f, y_min, y_max, lambda x: x_min, lambda x: x_max)

# 计算二重积分的近似值
approx_value = composite_simpson(lambda y: composite_simpson(lambda x: f(x, y), x_min, x_max, m), y_min, y_max, m)

# 计算误差
error_estimate = abs(actual_value - approx_value)

# 输出结果
print("二重积分的实际值：", actual_value)
print("使用复合辛普森公式计算的近似值：", approx_value)
print("误差估计：", error_estimate)
