import numpy as np  
  
# 定义被积函数f(x)  
def f(x):  
    return np.where(x != 0, np.sin(x) / x, 1)
  
# 牛顿-科茨公式的权重和节点，从1阶到7阶  
# 权重数组中的每个元素对应于相应阶数公式中的权重  
# 注意：高阶的牛顿-科茨公式可能不稳定，特别是当阶数较高时  
weights_nc = {  
    1: [0.5, 0.5],                       # 梯形公式（1阶）  
    2: [1/3, 4/3, 1/3],                  # 辛普森公式（2阶）  
    3: [3/8, 9/8, 9/8, 3/8],             # 3/8公式（3阶）  
    # 更高阶的权重可以根据需要添加，但请注意高阶公式的数值稳定性  
}  
  
# 定义使用牛顿-科茨公式计算积分的函数  
def newton_cotes_integration(f, a, b, order):  
    if order not in weights_nc:  
        raise ValueError(f"Newton-Cotes formula of order {order} is not supported.")  
      
    n = order + 1  # 节点数量  
    h = (b - a) / (n - 1)  # 步长  
    x_values = np.linspace(a, b, n)  # 生成等距节点  
    y_values = f(x_values)  # 计算节点处的函数值  
      
    integral = 0  
    for i, weight in enumerate(weights_nc[order]):  
        integral += weight * y_values[i]  
      
    integral *= h  
    return integral  
  
# 设置积分区间  
a = 0  # 积分下限  
b = 1  # 积分上限  
  
# 使用不同阶数的牛顿-科茨公式计算积分  
for order in range(1, 8):  # 阶数从1到7  
    if order in weights_nc:  
        integral = newton_cotes_integration(f, a, b, order)  
        print(f"The integral of f(x) from {a} to {b} using Newton-Cotes formula of order {order} is: {integral}")  
    else:  
        print(f"Newton-Cotes formula of order {order} is not implemented.")