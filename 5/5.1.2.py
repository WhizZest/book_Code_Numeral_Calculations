import numpy as np  
  
# 定义函数  
def f(x):  
    return np.exp(-x)  
  
# 梯形公式  
def trapezoidal_rule(a, b, n):  
    h = (b - a) / n  
    x = np.linspace(a, b, n+1)  
    y = f(x)  
    integral = h * (y[0]/2 + np.sum(y[1:-1]) + y[-1]/2)  
    return integral  
  
# 辛普森公式  
def simpson_rule(a, b, n):  
    if n % 2 != 0:  
        raise ValueError("n must be an even number for Simpson's rule")  
    h = (b - a) / n  
    x = np.linspace(a, b, n+1)  
    y = f(x)  
    integral = h/3 * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]))  
    return integral  
  
# 真实积分值（解析解）  
true_integral = 1 - 1/np.e  
  
# 使用梯形公式计算积分  
n = 100  # 可以调整n的值来观察精度变化  
trapezoidal_approx = trapezoidal_rule(0, 1, 1)  
print(f"Trapezoidal Approximation: {trapezoidal_approx}")  
print(f"Error (Trapezoidal): {abs(true_integral - trapezoidal_approx)}")  
  
# 使用辛普森公式计算积分  
simpson_approx = simpson_rule(0, 1, 2)  
print(f"Simpson Approximation: {simpson_approx}")  
print(f"Error (Simpson): {abs(true_integral - simpson_approx)}")