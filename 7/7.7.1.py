import numpy as np

# 定义非线性方程组
def equations(x):
    x1, x2 = x
    return [x1 + np.cos(x2) - 1, -np.sin(x1) + x2 - 1]

# 不动点迭代方法
def fixed_point_iteration(x0, tol=1e-16, max_iter=1000):
    x1, x2 = x0
    iterations = 0
    while True:
        x1_new = 1 - np.cos(x2)
        x2_new = 1 + np.sin(x1)
        iterations += 1
        if np.max(np.abs(np.array([x1_new, x2_new]) - np.array([x1, x2]))) < tol or iterations >= max_iter:
            break
        x1, x2 = x1_new, x2_new
    return np.array([x1, x2]), iterations

# 高斯–赛德尔方式
def gauss_seidel(x0, tol=1e-16, max_iter=1000):
    x1, x2 = x0
    iterations = 0
    while True:
        x1_new = 1 - np.cos(x2)
        x2 = 1 + np.sin(x1_new)
        iterations += 1
        if np.abs(x1_new - x1) < tol or iterations >= max_iter:
            break
        x1 = x1_new
    return np.array([x1_new, x2]), iterations

# 牛顿法
def newton_method(x0, tol=1e-16, max_iter=1000):
    x = np.array(x0, dtype=float)
    iterations = 0
    while True:
        J = np.array([
            [1, -np.sin(x[1])],
            [-np.cos(x[0]), 1]
        ])
        f = equations(x)
        delta_x = np.linalg.solve(J, -np.array(f))
        x += delta_x
        iterations += 1
        if np.linalg.norm(delta_x) < tol or iterations >= max_iter:
            break
    return x, iterations

# 初始猜测值
initial_guess = [-1, 1]
tol=2.2204e-16

# 不动点迭代法
result, iterations_fixed_point = fixed_point_iteration(initial_guess, tol)
print("Fixed Point Iteration:")
print("Solution:", result)
print("Iterations:", iterations_fixed_point)

# 高斯–赛德尔方式
result, iterations_gauss_seidel = gauss_seidel(initial_guess, tol)
print("\nGauss-Seidel Method:")
print("Solution:", result)
print("Iterations:", iterations_gauss_seidel)

# 牛顿法
result, iterations_newton = newton_method(initial_guess, tol)
print("\nNewton's Method:")
print("Solution:", result)
print("Iterations:", iterations_newton)
