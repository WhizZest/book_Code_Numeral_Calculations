import numpy as np  
from sympy import symbols, Eq, solve, sin, cos, diff, lambdify  
  
# 定义变量  
x1, x2 = symbols('x1 x2')  
  
# 不动点迭代方法  
def fixed_point_iteration(x1_init, x2_init, max_iter=1000, tol=1e-16):  
    x1_k, x2_k = x1_init, x2_init  
    for k in range(max_iter):  
        x1_k_new = 1 - np.cos(x2_k)  
        x2_k_new = 1 + np.sin(x1_k)  
        if abs(x1_k_new - x1_k) < tol and abs(x2_k_new - x2_k) < tol:  
            return x1_k_new, x2_k_new, k + 1  
        x1_k, x2_k = x1_k_new, x2_k_new  
    return x1_k, x2_k, max_iter  
  
# 高斯-赛德尔迭代方法  
def gauss_seidel(x1_init, x2_init, max_iter=1000, tol=1e-16):  
    x1_k, x2_k = x1_init, x2_init  
    for k in range(max_iter):  
        x1_k_old, x2_k_old = x1_k, x2_k  
        x1_k = 1 - np.cos(x2_k_old)  
        x2_k = 1 + np.sin(x1_k)  
        if abs(x1_k - x1_k_old) < tol and abs(x2_k - x2_k_old) < tol:  
            return x1_k, x2_k, k + 1  
    return x1_k, x2_k, max_iter  
  
# 牛顿法  
def newton_method(x1_init, x2_init, max_iter=1000, tol=1e-16):  
    J = np.array([[1, -np.sin(x2_init)], [-np.cos(x1_init), 1]])  
    F = np.array([x1_init + np.cos(x2_init) - 1, -np.sin(x1_init) + x2_init - 1])  
    x = np.array([x1_init, x2_init])  
      
    for k in range(max_iter):  
        delta_x = np.linalg.solve(J, -F)  
        x_new = x + delta_x  
        F_new = np.array([x_new[0] + np.cos(x_new[1]) - 1, -np.sin(x_new[0]) + x_new[1] - 1])  
        if np.linalg.norm(F_new) < tol:  
            return x_new[0], x_new[1], k + 1  
        J = np.array([[1, -np.sin(x_new[1])], [-np.cos(x_new[0]), 1]])  
        F = F_new  
        x = x_new  
    return x[0], x[1], max_iter  
  
# 初始值  
x1_init, x2_init = -1, 1  
max_iter=1000
tol=2.2204e-16
  
# 执行各种方法  
print("Fixed Point Iteration:")  
x1_fpi, x2_fpi, iter_fpi = fixed_point_iteration(x1_init, x2_init, max_iter, tol)  
print(f"Solution: x1 = {x1_fpi}, x2 = {x2_fpi}, Iterations: {iter_fpi}")  
  
print("\nGauss-Seidel Method:")  
x1_gs, x2_gs, iter_gs = gauss_seidel(x1_init, x2_init, max_iter, tol)  
print(f"Solution: x1 = {x1_gs}, x2 = {x2_gs}, Iterations: {iter_gs}")  
  
print("\nNewton's Method:")  
x1_nm, x2_nm, iter_nm = newton_method(x1_init, x2_init, max_iter, tol)  
print(f"Solution: x1 = {x1_nm}, x2 = {x2_nm}, Iterations: {iter_nm}")