import numpy as np  
  
# 定义被积函数  
def f(x, y):  
    return np.sin(x + y)  # 示例函数：sin(x + y)  
  
# 蒙特卡罗方法计算二重积分  
def monte_carlo_double_integration(f, a, b, c, d, N):  
    x_samples = np.random.uniform(a, b, N)  # 在区间 [a, b] 内随机生成 N 个 x 点  
    y_samples = np.random.uniform(c, d, N)  # 在区间 [c, d] 内随机生成 N 个 y 点  
    f_samples = f(x_samples, y_samples)  # 计算这些点上函数的值  
    average_f = np.mean(f_samples)  # 计算函数值的平均值  
    area = (b - a) * (d - c)  # 矩形区域的面积  
    integral = area * average_f  # 估计二重积分值  
    return integral  
  
# 设置积分区域和样本数量  
a, b = 0, np.pi / 2 # x 的范围  
c, d = 0, np.pi / 4 # y 的范围  
N = 100000  # 样本数量，增加样本数量可以提高精度  
  
# 使用蒙特卡罗方法计算二重积分  
integral = monte_carlo_double_integration(f, a, b, c, d, N)  
print("蒙特卡罗方法计算的二重积分值：", integral)