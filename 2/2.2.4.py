import numpy as np

# 定义分块矩阵A1、B、C、D
A1 = np.array([[3, 1],
               [4, 2]])

B = np.array([[2, 0],
              [0, 2]])

C = B

D = np.array([[5, 3],
              [1, 8]])

# 计算分块三角分解
D_11 = np.linalg.inv(A1)
L_11 = A1
U_11 = A1
U_12 = np.linalg.inv(A1).dot(B)
L_21 = C.dot(np.linalg.inv(A1))
L_22 = D - L_21.dot(U_12)

# 打印结果
print("D_11:")
print(D_11)
print("\nL_11:")
print(L_11)
print("\nU_11:")
print(U_11)
print("\nU_12:")
print(U_12)
print("\nL_21:")
print(L_21)
print("\nL_22:")
print(L_22)
