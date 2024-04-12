import numpy as np  
  
# 给定的数据点  
x_values = np.array([2.5, 2.6, 2.7, 2.8, 2.9, 3.0])  
y_values = np.array([12.1825, 13.4637, 14.8797, 16.4446, 18.1741])  # 这里去掉了x=3.0时的y值，因为我们不使用它  
  
# 二点后向差分公式计算x=2.7处的一阶导数  
h = 0.1  # 步长  
two_point_derivative = (y_values[2] - y_values[1]) / h  # 使用x=2.7和x=2.6的数据点  
  
# 三点中心差分公式计算x=2.7处的一阶导数  
three_point_derivative = (y_values[3] - y_values[1]) / (2 * h)  # 使用x=2.8, x=2.7(这个值在计算中不直接使用，但它是选择相邻点的基准)和x=2.6的数据点  
  
print(f"二点公式计算的一阶导数值: {two_point_derivative}")  
print(f"三点公式计算的一阶导数值: {three_point_derivative}")