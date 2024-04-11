import numpy as np
from scipy.special import roots_hermite
from scipy.integrate import quad
from sympy import symbols, integrate, exp, cos, oo  

def f_gauss(x):
    return np.cos(x)

def f_quad(x):
    return np.exp(-x ** 2) * np.cos(x)

# 定义积分函数
def accumulate_integral():
    # 定义变量  
    x = symbols('x')  
    
    # 定义被积函数  
    integrand = exp(-x**2) * cos(x)  
    
    # 使用SymPy的integrate函数计算定积分  
    actual_integral = integrate(integrand, (x, -oo, oo))  
    
    return actual_integral

# 获取五点高斯–埃尔米特节点和权重
x, w = roots_hermite(5)

# 计算积分值的近似值
approx_integral = np.sum(w * f_gauss(x))

# 计算quad积分值
quad_integral, _ = quad(f_quad, -np.inf, np.inf)

# 计算实际积分值
actual_integral = accumulate_integral()

print("近似积分值为:", approx_integral)
print("quad积分值为:", quad_integral)
print("实际积分值为:", actual_integral, "=", actual_integral.evalf())
