import numpy as np  
  
def f(x):  
    # 当x为0时，f(x)的值为1（根据洛必达法则）  
    if x == 0:  
        return 1  
    else:  
        return np.sin(x) / x  
  
def trapezoidal_rule(a, b, n):  
    h = (b - a) / n  
    s = (f(a) + f(b)) / 2  
    for i in range(1, n):  
        s += f(a + i * h)  
    return s * h  
  
def romberg_integration(a, b, epsilon=1e-7, max_iter=100):  
    # 初始化R矩阵  
    R = np.zeros((max_iter, max_iter))  
    R[0, 0] = (b - a) * (f(a) + f(b)) / 2  # 使用一个区间的梯形法则  
    print(f"R[0, 0] = {R[0, 0]}")  # 打印初始梯形法则结果  
  
    for j in range(1, max_iter):  
        n = 2**j  
        h = (b - a) / n  
        sum_y = 0  
        for i in range(1, n, 2):  
            sum_y += f(a + i * h)  
        R[j, 0] = R[j-1, 0] / 2 + h * sum_y  
        print(f"R[{j}, 0] = {R[j, 0]}")  # 打印当前梯形法则结果  
  
        # 应用Richardson外推  
        for k in range(1, j+1):  
            R[j, k] = (4**k * R[j, k-1] - R[j-1, k-1]) / (4**k - 1)  
            print(f"R[{j}, {k}] = {R[j, k]}")  # 打印当前Richardson外推结果  
  
            # 检查是否达到所需精度  
            if j > k and abs(R[j, k] - R[j-1, k-1]) < epsilon:  
                print(f"Converged at R[{j}, {k}] with value {R[j, k]}")  
                return R[j, k]  
  
    raise ValueError("The required accuracy was not achieved within the maximum number of iterations.")
  
# 使用龙贝格方法计算积分  
a, b = 0, 1  # 积分下限和上限  
integral = romberg_integration(a, b)  
print(f"The integral of sin(x)/x from {a} to {b} is approximately: {integral}")