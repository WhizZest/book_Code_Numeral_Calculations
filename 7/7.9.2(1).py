import numpy as np  
from scipy.optimize import fsolve, newton  
import math  
  
# （1）求f(x) = x^3 + x - 6的根，取初值x0 = 1  
  
def f(x):  
    return x**3 + x - 6  
  
def solve_cubic_equation():  
    x0 = 1  
    root = newton(f, x0)  
    print(f"The root of f(x) = x^3 + x - 6 is: {root}")  
  
# （2）求非线性方程组 {x1 + cos(x2) - 1 = 0, -sin(x1) + x2 - 1 = 0} 的根，取初值[-1, 1]^T  
  
def equations(vars):  
    x, y = vars  
    eq1 = x + math.cos(y) - 1  
    eq2 = -math.sin(x) + y - 1  
    return [eq1, eq2]  
  
def solve_nonlinear_equations():  
    x0 = [-1, 1]  
    sol = fsolve(equations, x0)  
    print(f"The roots of the nonlinear equations are: {sol}")  
  
if __name__ == "__main__":  
    solve_cubic_equation()  
    solve_nonlinear_equations()