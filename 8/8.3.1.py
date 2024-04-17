import numpy as np  
from scipy.linalg import qr  
import matplotlib.pyplot as plt
  
def qr_algorithm(A, num_iterations=100, tol=1e-10): 
    # 计算对角线特征值的函数
    def calculate_eigenvalues(A):  
        # 特征值为收敛后的Ak的对角线元素，可能是1x1或2x2块  
        eigenvalues = []  
        n = len(A)  
        i = 0  
        while i < n:  
            if i + 1 < n and np.abs(A[i+1, i]) > tol and np.abs(A[i, i+1]) > tol:  # 检查是否为2x2块  
                # 使用公式计算2x2块的特征值  
                a = A[i, i]  
                b = A[i, i+1]  
                c = A[i+1, i]  
                d = A[i+1, i+1]  
                eigenvalues.extend(np.linalg.eigvals([[a, b], [c, d]]))  
                i += 2  
            else:  
                eigenvalues.append(A[i, i])  
                i += 1  
        return eigenvalues 
    
    Ak = np.copy(A)  
    n = A.shape[0]  
    iterations = 0  
    errs1 = []
    errs2 = []
    errs3 = []
    errs4 = []
    errs5 = []
    errs6 = []
    for k in range(num_iterations):  
        eigenvaluesK = calculate_eigenvalues(Ak)
        # 进行QR分解  
        Q, R = qr(Ak)  
          
        # 形成新的Ak+1  
        Ak_next = R.dot(Q)  
        eigenvaluesK_next = calculate_eigenvalues(Ak_next)
        
        errs6.append(np.linalg.norm(np.diag(Ak_next) - np.diag(Ak)))# 检查收敛条件：||diag(Ak+1) - diag(Ak)|| < tol  
        #errs2.append(np.linalg.norm(np.tril(Ak_next, k=-1) - np.tril(Ak, k=-1)))#比较不含对角线的下三角矩阵
        errs1.append(np.abs(Ak_next[1, 0] - Ak[1, 0]))
        errs2.append(np.abs(Ak_next[2, 1]))
        errs3.append(np.abs(Ak_next[3, 2] - Ak[3, 2]))
        dEig = np.abs(np.linalg.norm(eigenvaluesK_next) - np.linalg.norm(eigenvaluesK))
        errs4.append(dEig)
        errs5.append(len(eigenvaluesK_next) - len(eigenvaluesK))
        
        iterations += 1  
        if dEig < tol and len(eigenvaluesK_next) == len(eigenvaluesK): 
            Ak = Ak_next  
            break  
        Ak = Ak_next 
          
    eigenvalues = calculate_eigenvalues(Ak) 
              
    return np.array(eigenvalues), iterations, [errs1, errs2, errs3, errs4, errs5, errs6]
  
# 给定的矩阵A  
A = np.array([[5, -2, -5, -1],   
              [1, 0, -3, 2],   
              [0, 2, 2, -3],   
              [0, 0, 1, -2]], dtype=float)  
  
# 使用QR方法计算特征值并记录迭代次数  
eigenvalues, iterations, errors_data = qr_algorithm(A)  
print("特征值：", eigenvalues)  
print("迭代次数：", iterations)

# Plot the errors for each set of parameters
plt.figure(figsize=(10, 6))
for i, errors in enumerate(errors_data):
    plt.plot(range(1, len(errors) + 1), errors, marker='o', label=f'Tolerance={i + 1}')
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.title('Convergence of QR Algorithm with Different Tolerances')
plt.legend()
plt.grid(True)
plt.show()