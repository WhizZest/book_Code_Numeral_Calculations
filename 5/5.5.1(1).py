import numpy as np  
import math  
from sympy import symbols, sin, Integral, pi, simplify
  
# 定义被积函数，使用numpy的sin函数以支持数组输入  
def f(x, y):  
    return np.sin(x + y)  
  
# 辛普森公式单变量积分  
def simpson_rule_1d(a, b, n, f):  
    h = (b - a) / n  
    x = np.linspace(a, b, n+1)  
    y = f(x)  
    integral = h / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]))  
    return integral  
  
# 辛普森公式二重积分  
def simpson_rule_2d(x_range, y_range, nx, ny, f):  
    a, b = x_range  
    c, d = y_range  
    hx = (b - a) / nx
    xi = np.linspace(a, b, nx+1)
    Iy = np.array([simpson_rule_1d(c, d, ny, lambda y: f(x, y)) for x in xi])
    integral = hx / 3 * (Iy[0] + Iy[-1] + 4 * np.sum(Iy[1:-1:2]) + 2 * np.sum(Iy[2:-1:2]))
    return integral  
  
# 定义范围和分点数  
x_range = (0, math.pi / 2)  
y_range = (0, math.pi / 4)  
nx, ny = 4, 4  # 可以通过增加 nx, ny 来提高精度  
  
# 使用复合辛普森公式计算二重积分  
approx_integral = simpson_rule_2d(x_range, y_range, nx, ny, f)  
print(f"近似积分值: {approx_integral}")  
  
# 计算实际积分值（解析解）  
# 对于这个函数，我们可以手动计算出精确的二重积分值  
# ∫(from 0 to π/4) ∫(from 0 to π/2) sin(x+y) dx dy  
x, y = symbols('x y')  
actual_integral = Integral(Integral(sin(x + y), (x, 0, pi/2)), (y, 0, pi/4)).doit()  
actual_integral = simplify(actual_integral)  
print(f"实际积分值: {actual_integral}")  
  
# 计算误差  
error = abs(actual_integral - approx_integral)  
print(f"误差: {error}")