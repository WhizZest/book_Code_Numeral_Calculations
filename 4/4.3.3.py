import numpy as np  
import matplotlib.pyplot as plt  
from scipy.special import legendre  
from scipy.linalg import lstsq  
from sympy import symbols, legendre_poly, simplify
  
# 定义被逼近的函数 f(x) = sqrt(x)  
def f(x):  
    return np.sqrt(x)  
  
# 将[0, 1]区间变换到[-1, 1]区间  
def transform_x(x):  
    return 2 * x - 1  

# 打印转换前和转换后的多项式
def printCoeffs(coeff):  
    # 定义变量  
    x,t = symbols('x t')  
    
    # 根据系数构造多项式  
    poly_expr = sum(coeff * t**i for i, coeff in enumerate(coeffs))  
    simplified_poly_expr = simplify(poly_expr)
    print("Transformed polynomial:", simplified_poly_expr)

    # 进行变量替换 t' = 2x - 1  
    substituted_poly = poly_expr.subs(t, 2*x - 1)  

    # 化简多项式  
    simplified_poly = simplify(substituted_poly) 
    
    # 打印转换后的多项式  
    print(f"Original polynomial: {simplified_poly}")
    return simplified_poly, simplified_poly_expr

# 在[0, 1]区间内生成采样点  
x_values = np.linspace(0, 1, 1000)  
transformed_x = transform_x(x_values)  
  
# 计算对应的f(x)值  
y_values = f(x_values)  
  
# 选择勒让德多项式的最高次数  
degree = 1  
  
# 构造勒让德多项式的设计矩阵  
A = np.vstack([legendre(i)(transformed_x) for i in range(degree + 1)]).T  
  
# 使用最小二乘法求解系数  
coeffs, _, _, _ = lstsq(A, y_values)  

# 打印系数  
print("勒让德多项式的系数:")  
simplified_poly, simplified_poly_expr = printCoeffs(coeffs)  
# 构造逼近多项式  
def approximant(x):  
    total = 0  
    transformed_x = transform_x(x)  
    for i, c in enumerate(coeffs):  
        total += c * legendre(i)(transformed_x)  
    return total  
  
# 绘制对比图像  
plt.figure(figsize=(10, 6))  
plt.plot(x_values, y_values, label=r'$f(x) = \sqrt{x}$')  
plt.plot(x_values, approximant(x_values), label=simplified_poly, linestyle='--')  
#plt.scatter(x_values, y_values, color='red', s=10)  # 采样点  
plt.xlabel('x')  
plt.ylabel('y')  
plt.title('Legendre Polynomial Approximation of sqrt(x) on [0, 1]')  
plt.legend()  
plt.grid(True)  
plt.show()