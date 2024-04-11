import numpy as np  
  
def f(x):  
    return np.where(x == 0, 1, np.sin(x) / x) 
  
def trapezoidal_rule(a, b, n):  
    h = (b - a) / n  
    x_values = np.linspace(a, b, n+1)  
    y_values = f(x_values)  
    return h * (0.5*y_values[0] + 0.5*y_values[-1] + np.sum(y_values[1:-1]))  
  
def trapezoidal_integration(a, b, tolerance=1e-7):  
    n = 1  # 初始步数为1
    Tn = trapezoidal_rule(a, b, n)  
    iteration = 0  
    while True:  
        iteration += 1  
        T2n = trapezoidal_rule(a, b, 2*n) 
        print(f"Iteration {iteration} : Approximate integral: {T2n}")  
        if abs(T2n - Tn) <= tolerance:  
            print(f"Convergence reached after {iteration} iterations.")  
            return T2n  
        Tn = T2n  
        n *= 2  
  
# 计算并打印积分值  
integral = trapezoidal_integration(0, 1)  
print(f"The integral of sin(x)/x from 0 to 1 is approximately: {integral}")