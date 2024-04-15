import numpy as np

# 定义矩阵 A 和向量 b
A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 4]])
b = np.array([3, 2, 3])

# 最速下降法
def steepest_descent(A, b, x0, tol=1e-6, max_iter=1000):
    x = x0
    r = b - np.dot(A, x)  # 计算初始残差
    iteration = 0
    for k in range(max_iter):
        alpha = np.dot(r, r) / np.dot(np.dot(r, A), r)  # 计算步长
        x = x + alpha * r  # 更新解
        r = b - np.dot(A, x)  # 更新残差
        iteration += 1
        if np.linalg.norm(r) < tol:  # 检查是否满足收敛条件
            break
    return x, iteration

# 共轭梯度法
def conjugate_gradient(A, b, x0, tol=1e-6, max_iter=1000):
    x = x0
    r = b - np.dot(A, x)  # 计算初始残差
    p = r  # 初始化搜索方向
    iteration = 0
    for k in range(max_iter):
        alpha = np.dot(r, r) / np.dot(np.dot(p, A), p)  # 计算步长
        x = x + alpha * p  # 更新解
        r_new = r - alpha * np.dot(A, p)  # 更新残差
        iteration += 1

        if np.linalg.norm(r_new) < tol:  # 检查是否满足收敛条件
            break
        beta = np.dot(r_new, r_new) / np.dot(r, r)  # 计算新的搜索方向
        p = r_new + beta * p  # 更新搜索方向
        r = r_new
    return x, iteration
# 左预处理最速下降法
def precond_steepest_descent(A, b, x0, M, tol=1e-6, max_iter=1000):
    x = x0
    r = b - np.dot(A, x)  # 计算初始残差
    iteration = 0
    for k in range(max_iter):
        z = np.linalg.solve(M, r)  # 预处理残差
        alpha = np.dot(z, r) / np.dot(np.dot(z, A), z)  # 计算步长
        x = x + alpha * z  # 更新解
        r = b - np.dot(A, x)  # 更新残差
        iteration += 1
        if np.linalg.norm(r) < tol:  # 检查是否满足收敛条件
            break
    return x, iteration

# 左预处理共轭梯度法
def precond_conjugate_gradient(A, b, x0, M, tol=1e-6, max_iter=1000):
    x = x0
    r = b - np.dot(A, x)  # 计算初始残差
    z = np.linalg.solve(M, r)  # 预处理初始残差
    p = z  # 初始化搜索方向
    iteration = 0
    for k in range(max_iter):
        alpha = np.dot(z, r) / np.dot(np.dot(p, A), p)  # 计算步长
        x = x + alpha * p  # 更新解
        r_new = r - alpha * np.dot(A, p)  # 更新残差
        z_new = np.linalg.solve(M, r_new)  # 预处理残差
        beta = np.dot(z_new, r_new) / np.dot(z, r)  # 计算新的搜索方向
        p = z_new + beta * p  # 更新搜索方向
        r = r_new
        z = z_new
        iteration += 1
        if np.linalg.norm(r) < tol:  # 检查是否满足收敛条件
            break
    return x, iteration

# 初始解
x0 = np.zeros_like(b)

# 使用最速下降法求解
solution_sd, iterations_sd = steepest_descent(A, b, x0)
print("Solution using steepest descent method:", solution_sd)
print("Iterations:", iterations_sd)

# 使用共轭梯度法求解
solution_cg, iterations_cg = conjugate_gradient(A, b, x0)
print("Solution using conjugate gradient method:", solution_cg)
print("Iterations:", iterations_cg)

# 左预处理矩阵 M
M = np.diag(np.diag(A))
# 使用左预处理最速下降法求解
solution_psd, iterations_psd = precond_steepest_descent(A, b, x0, M)
print("Solution using preconditioned steepest descent method:", solution_psd)
print("Iterations:", iterations_psd)

# 使用左预处理共轭梯度法求解
solution_pcg, iterations_pcg = precond_conjugate_gradient(A, b, x0, M)
print("Solution using preconditioned conjugate gradient method:", solution_pcg)
print("Iterations:", iterations_pcg)