import matplotlib.pyplot as plt  
import numpy as np  
  
# 定义Fibonacci序列生成器  
def fibonacci(n):  
    if n <= 1:  
        return n  
    a, b = 0, 1  
    for i in range(2, n + 1):  
        a, b = b, a + b  
    return b  
  
# 定义四个序列的函数  
def sequence1(k):  
    return 2 ** (1 - k)  
  
def sequence2(k):  
    return 0.9 ** (k - 1)  
  
def sequence3(k):  
    F_k_plus_1 = fibonacci(k + 1)  
    return 2 ** (1 - F_k_plus_1)  
  
def sequence4(k):  
    return 2 ** (2 - 2 ** k)  
  
# 生成k值和对应的序列值  
k_values = np.arange(1, 21)  # 考察k从1到20的变化  
s1_values = [sequence1(float(k)) for k in k_values]
s2_values = [sequence2(k) for k in k_values]  
s3_values = [sequence3(k) for k in k_values]  
s4_values = [sequence4(float(k)) for k in k_values]  
  
# 绘制图形  
plt.figure(figsize=(12, 6))  
  
plt.plot(k_values, s1_values, label='2^(1-k)')  
plt.plot(k_values, s2_values, label='0.9^(k-1)')  
plt.plot(k_values, s3_values, label='2^(1-F_(k+1))')  
plt.plot(k_values, s4_values, label='2^(2-2^k)')  
  
plt.xlabel('k')  
plt.ylabel('Sequence Value')  
plt.title('Convergence Speed of Four Sequences')  
plt.legend()  
plt.yscale('log')  # 使用对数刻度以更好地显示收敛情况  
plt.grid(True)  
plt.show()