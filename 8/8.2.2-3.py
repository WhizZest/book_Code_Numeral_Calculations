import numpy as np  
  
def power_method(A, epsilon=1e-10, max_iterations=1000):  
    """乘幂法计算模最大的特征值和特征向量"""  
    n = A.shape[0]  
    x = [1.0, 0.5, -0.5]#np.random.rand(n)  
    x = x / np.linalg.norm(x)  
    lambda_old = None  
    iteration = 0  
    for iteration in range(max_iterations):  
        y = np.dot(A, x)  
        lambda_new = np.dot(x, y) / np.dot(x, x)  
        # 欧几里得范数
        #x = y / np.linalg.norm(y)  
        # 无穷范数
        x = y / np.linalg.norm(y, np.inf)
        if lambda_old is not None and abs(lambda_new - lambda_old) < epsilon:  
            break  
        lambda_old = lambda_new  
    print(f"乘幂法迭代次数: {iteration + 1}")  
    return lambda_new, x  
  
def inverse_power_method(A, sigma, epsilon=1e-10, max_iterations=1000):  
    """带原点平移的反幂法计算模最小的特征值和特征向量"""  
    n = A.shape[0]  
    x = [1.0, 0.5, -0.5]#np.random.rand(n)  
    x = x / np.linalg.norm(x)  
    I = np.eye(n)  
    B = A - sigma * I  
    mu_old = None  
    iteration = 0  
    for iteration in range(max_iterations):  
        # 使用线性求解器而不是直接求逆  
        y = np.linalg.solve(B, x)   
        mu = np.dot(x, y)  
        # 欧几里得范数
        x_new = y / np.linalg.norm(y)
        lambda_new = 1 / mu + sigma  
        if mu_old is not None and abs(1/mu - 1/mu_old) < epsilon:  
            break  
        x = x_new  
        mu_old = mu  
    print(f"带原点平移的反幂法迭代次数: {iteration + 1}")  
    return lambda_new, x  

def inverse_power_method_simple(A, epsilon=1e-10, max_iterations=1000):  
    """简化的反幂法计算模最小的特征值和特征向量"""  
    n = A.shape[0]  
    x = [1.0, 0.5, -0.5]#np.random.rand(n)  
    x = x / np.linalg.norm(x)  
    A_inv = np.linalg.inv(A) 
    lambda_old = None
    iteration = 0  
    for iteration in range(max_iterations):  
        # 使用线性求解器而不是直接求逆  
        y = np.linalg.solve(A, x) 
        index_max_abs = np.argmax(np.abs(y))
        lambda_new = y[index_max_abs]
        x_new = y / lambda_new
        if lambda_old is not None and abs(1/lambda_new - 1/lambda_old) < epsilon:  
            break  
        x = x_new  
        lambda_old = lambda_new
    print(f"简化的反幂法迭代次数: {iteration + 1}")  
    return 1/lambda_new, x  
  
# 验证给定特征值和特征向量是否是矩阵的特征值
def is_eigenvalue(A, lambda_val, eigen_vector):
    # 计算 Ax  
    Ax = np.dot(A, eigen_vector)  
    
    # 计算 lambda * x  
    lambda_x = lambda_val * eigen_vector  
    
    # 检查是否相等（考虑到浮点数的精度问题，我们使用 np.allclose 进行比较）  
    if np.allclose(Ax, lambda_x):  
        print("验证成功，给定的 lambda 和 向量 是矩阵 A 的一个特征值和特征向量。")  
    else:  
        print("验证失败，给定的 lambda 不是矩阵 A 的特征值。")

A = np.array([[12, 6, -6], [6, 16, 2], [-6, 2, 16]])  
  
# 乘幂法计算模最大的特征值和特征向量  
largest_eigenvalue, largest_eigenvector = power_method(A)  
print(f"模最大的特征值: {largest_eigenvalue}")  
print(f"对应的特征向量: {largest_eigenvector}")  
  
# 为了使用带原点平移的反幂法，我们首先需要一个接近最小特征值的估计值。  
# 简化起见，这里我们使用0作为估计值。在实际应用中，可能需要更精确的估计。  
smallest_eigenvalue, smallest_eigenvector = inverse_power_method(A, sigma=0)  
print(f"模最小的特征值: {smallest_eigenvalue}")  
print(f"对应的特征向量: {smallest_eigenvector}")
is_eigenvalue(A, smallest_eigenvalue, smallest_eigenvector)

# 反幂法
smallest_eigenvalue_simple, smallest_eigenvector_simple = inverse_power_method_simple(A)
print(f"模最小的特征值: {smallest_eigenvalue_simple}")
print(f"对应的特征向量: {smallest_eigenvector_simple}")
is_eigenvalue(A, smallest_eigenvalue_simple, smallest_eigenvector_simple)
