import numpy as np

# 定义函数
def f(x):
    return np.where(x == 0, 1, np.sin(x) / x)

# 变步长梯形公式计算积分
def adaptive_trapezoidal(f, a, b, tol):
    n = 1  # 初始区间数
    T_n = (b - a) * (f(a) + f(b)) / 2  # 初始积分值
    h = b - a  # 初始步长
    
    while True:
        # 将积分区间分割为 n 个子区间
        x = np.linspace(a, b, n+1)
        
        # 计算子区间上的梯形积分值
        T_2n = T_n / 2 + h / 2 * np.sum(f((x[:-1] + x[1:]) / 2))
        
        # 判断是否满足精度要求
        if np.abs(T_2n - T_n) < tol:
            return T_2n
        
        # 更新变量以进行下一次迭代
        n *= 2
        T_n = T_2n
        h /= 2

# 积分区间
a = 0
b = 1

# 精度要求
tolerance = 1e-7

# 使用变步长梯形公式计算积分
integral = adaptive_trapezoidal(f, a, b, tolerance)

# 打印积分值
print("积分值:", integral)

# 打印积分区间等分的份数
partition_length = 0.1  # 每份的长度
num_partitions = int((b - a) / partition_length)
print("积分区间等分的份数:", num_partitions)
