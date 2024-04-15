import numpy as np  
  
# 定义系数矩阵A和向量b  
A = np.array([[2, -1, 0],
              [-1, 3, -1],
              [0, -1, 2]], dtype=float)  
b = np.array([1, 8, -5], dtype=float)  
  
# 初始化解向量x  
x = np.zeros_like(b)  
  
# 迭代次数和容忍误差  
max_iterations = 1000  
tolerance = 1e-4  
  
# 雅可比迭代法  
def jacobi_iteration(A, b, x0, max_iterations, tolerance):  
    D = np.diag(np.diag(A))  
    LU = A - D  
    x = x0.copy()  
    for iteration in range(max_iterations):  
        D_inv = np.diag(1 / np.diag(D))  
        x_new = np.dot(D_inv, b - np.dot(LU, x))  
        if np.linalg.norm(x_new - x) < tolerance:  
            return iteration + 1, x_new  
        x = x_new  
    return iteration + 1, x  
  
# 高斯-赛德尔迭代法  
def gauss_seidel_iteration(A, b, x0, max_iterations, tolerance):  
    x = x0.copy()  
    for iteration in range(max_iterations):  
        x_new = x.copy()  
        for j in range(A.shape[0]):  
            s1 = np.dot(A[j, :j], x_new[:j])  
            s2 = np.dot(A[j, j + 1:], x[j + 1:])  
            x_new[j] = (b[j] - s1 - s2) / A[j, j]  
        if np.linalg.norm(x_new - x) < tolerance:  
            return iteration + 1, x_new  
        x = x_new  
    return iteration + 1, x  
  
# 逐次超松弛迭代法 (SOR)  
def sor_iteration(A, b, x0, omega, max_iterations, tolerance):  
    x = x0.copy()  
    D = np.diag(np.diag(A))  
    LU = A - D  
    for iteration in range(max_iterations):  
        x_old = x.copy()  
        for j in range(A.shape[0]):  
            old_xj = x_old[j]  
            s1 = np.dot(A[j, :j], x[:j])  
            s2 = np.dot(A[j, j + 1:], x_old[j + 1:])  
            x[j] = (1 - omega) * old_xj + (omega / A[j, j]) * (b[j] - s1 - s2)  
        if np.linalg.norm(x - x_old) < tolerance:  
            return iteration + 1, x  
    return iteration + 1, x  

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
    return iteration, x

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
        beta = np.dot(r_new, r_new) / np.dot(r, r)  # 计算新的搜索方向
        p = r_new + beta * p  # 更新搜索方向
        r = r_new
        iteration += 1
        if np.linalg.norm(r) < tol:  # 检查是否满足收敛条件
            break
    return iteration, x
  
# 设置SOR的松弛因子  
omega = 1.1  
  
# 执行多种迭代方法并记录迭代次数  
iterations_jacobi, x_jacobi = jacobi_iteration(A, b, x, max_iterations, tolerance)  
iterations_gauss_seidel, x_gauss_seidel = gauss_seidel_iteration(A, b, x, max_iterations, tolerance)  
iterations_sor, x_sor = sor_iteration(A, b, x, omega, max_iterations, tolerance) 
iterations_sd, x_sd = steepest_descent(A, b, x, tolerance, max_iterations)
iterations_cg, x_cg = conjugate_gradient(A, b, x, tolerance, max_iterations)
  
# 输出结果  
print("Jacobi Iteration Solution:", x_jacobi)  
print("Jacobi Iteration Number of Iterations:", iterations_jacobi)  
print("Gauss-Seidel Iteration Solution:", x_gauss_seidel)  
print("Gauss-Seidel Iteration Number of Iterations:", iterations_gauss_seidel)  
print("SOR Iteration Solution:", x_sor)  
print("SOR Iteration Number of Iterations:", iterations_sor)
print("Solution using steepest descent method:", x_sd)
print("Iterations:", iterations_sd)
print("Solution using conjugate gradient method:", x_cg)
print("Iterations:", iterations_cg)