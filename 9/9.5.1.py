import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def finite_difference(N):
    h = 1/N

    # 构建系数矩阵
    A = np.zeros((N-1, N-1))
    for i in range(N-1):
        if i > 0:
            A[i][i-1] = -1 / h**2
        A[i][i] = 2 / h**2 + 1
        if i < N-2:
            A[i][i+1] = -1 / h**2

    # 构建右端向量
    b = [(np.pi**2 + 1) * np.sin(np.pi * (i+1) * h) for i in range(N-1)]

    # 解线性方程组
    y_approx = np.linalg.solve(A, b)

    return y_approx

def exact_solution(x):
    return np.sin(np.pi * x)

def error_norm(N):
    h = 1/N
    x = np.linspace(h, 1-h, N-1)
    y_approx = finite_difference(N)
    y_exact = exact_solution(x)
    error = np.abs(y_exact - y_approx)
    return np.max(error)

def format_scientific(num):
    return "{:.5e}".format(num)
def main():
    N_values = [2**k for k in range(1, 9)]
    error_norms = []

    for N in N_values:
        error_norms.append(error_norm(N))

    # 打印误差表格
    error_norms_scientific = [format_scientific(error) for error in error_norms]
    table_data = {'N': N_values, 'Error Infinity Norm': error_norms_scientific}
    error_table = pd.DataFrame(table_data)
    print(error_table)

    # 绘制误差无穷范数随网格大小变化的图表
    plt.plot(N_values, error_norms, marker='o')
    plt.xlabel('N')
    plt.ylabel('Infinity Norm of Error')
    plt.title('Convergence of Finite Difference Method')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
