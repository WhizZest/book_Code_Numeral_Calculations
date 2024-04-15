import numpy as np  
  
def steepest_descent(A, b, x0, tol=1e-6, max_iter=1000):  
    x = x0.copy()  
    r = b - np.dot(A, x)  
    iteration = 0  
    for i in range(max_iter):  
        p = r  # 最速下降法的搜索方向是负梯度方向  
        Ap = np.dot(A, p)  
        alpha = np.dot(r, r) / np.dot(p, Ap)  
        x += alpha * p  
        r = r - alpha * Ap  
        iteration += 1  
        if np.linalg.norm(r) < tol:  
            break  
    return x, iteration

def conjugate_gradient(A, b, x0, tol=1e-6, max_iter=1000):  
    x = x0.copy()  
    r = b - np.dot(A, x)  
    p = r.copy()  
    rsold = np.dot(r, r)  
    iteration = 0  
    for i in range(max_iter):  
        Ap = np.dot(A, p)  
        alpha = rsold / np.dot(p, Ap)  
        x += alpha * p  
        r_new = r - alpha * Ap  
        iteration += 1  
        if np.linalg.norm(r_new) < tol:  
            break  
        p_new = r_new + (np.dot(r_new, r_new) / rsold) * p  
        p = p_new  
        r = r_new  
        rsold = np.dot(r_new, r_new)  
    return x, iteration  
  
# 给定矩阵A和向量b  
A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]], dtype=float)  
b = np.array([3, 2, 3], dtype=float)  
  
# 初始解向量x0  
x0 = np.zeros_like(b)  
  
# 调用最速下降法函数  
x_sd, iterations_sd = steepest_descent(A, b, x0)  
print("最速下降法解:", x_sd)  
print("最速下降法迭代次数:", iterations_sd)

# 调用共轭梯度法函数  
x_cg, iterations_cg = conjugate_gradient(A, b, x0)  
print("共轭梯度法解:", x_cg)  
print("共轭梯度法迭代次数:", iterations_cg)