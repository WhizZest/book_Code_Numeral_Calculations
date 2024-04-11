import numpy as np
from scipy.integrate import quad

def f(x):
    if x == 0:
        return 1  # 处理 x = 0 时的情况
    else:
        return np.sin(x) / x

# 高斯–勒让德积分的权重和节点
nodes, weights = np.polynomial.legendre.leggauss(3)  # 指定阶数（节点数量将是 阶数+1）进行积分

# 将积分区间映射到[0, 1]区间
def transform(x):
    return 0.5 * x + 0.5

# 从0到1的积分
def integral():
    integral_value = 0
    for i in range(len(nodes)):
        integral_value += weights[i] * f(transform(nodes[i]))
    return 0.5 * integral_value

result, error = quad(f, 0, 1)  # 使用SciPy中的quad函数计算实际积分值

print("通过高斯–勒让德公式计算的积分值:", integral())
print("实际积分值（使用SciPy quad函数计算）:", result)
