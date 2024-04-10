import numpy as np

def givens_rotation(A):
    m, n = A.shape
    Q = np.eye(m)  # 初始化单位矩阵 Q
    R = np.copy(A)  # 初始化 R 矩阵为 A 的副本
    
    for j in range(n):
        for i in range(m-1, j, -1):  # 从下往上遍历每一列
            if R[i, j] != 0:  # 如果 R[i, j] 不为零，说明需要进行旋转操作
                c = R[j, j] / np.sqrt(R[j, j]**2 + R[i, j]**2)  # 计算旋转角的余弦值
                s = R[i, j] / np.sqrt(R[j, j]**2 + R[i, j]**2)  # 计算旋转角的正弦值
                
                # 构造 Givens 旋转矩阵
                G = np.array([[c, s],
                              [-s, c]])
                
                # 对 R 进行 Givens 变换
                R[[j, i], j:] = np.dot(G, R[[j, i], j:])
                
                # 对 Q 进行相应的变换
                Q[:, [j, i]] = Q[:, [j, i]].dot(G.T)
    
    return Q.T, R

# 给定矩阵 A
A = np.array([[4.8, 2.56, 2.528],
              [3.6, 4.92, 3.296],
              [0.0, 1.8, 1.84],
              [0.0, 0.0, 0.6]])

# 应用 Givens 变换得到上三角矩阵
Q, R = givens_rotation(A)

print("矩阵 Q：")
print(Q)
print("矩阵 R：")
print(R)
