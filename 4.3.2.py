import numpy as np  
import matplotlib.pyplot as plt  
from scipy.integrate import quad  
from scipy.linalg import solve  
from scipy.special import eval_legendre as P  
from scipy.special import legendre as legendre_poly
  
# 定义被逼近函数  
def f(x):  
    return np.exp(x)  
  
def legendre_polyval(coefficients, x):  
    """  
    Evaluate a series expansion in Legendre polynomials at points x.  
      
    Parameters:  
    coefficients : array_like  
        Coefficients of the Legendre series expansion in descending order  
        (i.e., coefficients[0] is the coefficient of P_n(x), where n is the  
        highest degree Legendre polynomial, coefficients[1] is the coefficient  
        of P_{n-1}(x), etc.).  
    x : array_like  
        Points at which to evaluate the series expansion.  
          
    Returns:  
    y : ndarray  
        Values of the Legendre series expansion at x.  
    """  
    # Initialize output array  
    y = np.zeros_like(x, dtype=float)  
      
    # Iterate over the coefficients and add the contribution of each Legendre polynomial  
    for i, coef in enumerate(coefficients):  
        y += coef * legendre_poly(i)(x)  
          
    return y  

# 定义勒让德多项式的积分  
def legendre_integral(n, m):  
    if n == m:  
        return 2.0 / (2.0 * n + 1.0)  
    else:  
        return 0.0  
  
# 计算逼近多项式的系数  
def compute_coefficients(n):  
    # 构建线性方程组的系数矩阵A和常数向量b  
    A = np.zeros((n+1, n+1))  
    b = np.zeros(n+1)  
    for i in range(n+1):  
        for j in range(n+1):  
            A[i, j] = legendre_integral(i, j)  
        b[i] = quad(lambda x: f(x) * P(i, x), -1, 1)[0]  
    # 解线性方程组Ax = b得到系数  
    coefficients = solve(A, b)  
    return coefficients 
  
# 主函数  
def main():  
    # 初始化绘图  
    plt.figure(figsize=(10, 6))  
  
    # 原始函数曲线  
    x = np.linspace(-1, 1, 1000)  
    y_true = f(x)  
    plt.plot(x, y_true, label='True function $e^x$', color='black')  
  
    # 计算并绘制S1(x)  
    coefficients_S1 = compute_coefficients(1)  
    print(f"Coefficients for S1(x): {coefficients_S1}")
    y_approx_S1 = legendre_polyval(coefficients_S1, x)  
    plt.plot(x, y_approx_S1, label=f'Approximation $S_1(x)$', linestyle='--')  
  
    # 计算并绘制S3(x)  
    coefficients_S3 = compute_coefficients(3)  
    print(f"Coefficients for S3(x): {coefficients_S3}")
    y_approx_S3 = legendre_polyval(coefficients_S3, x)  
    plt.plot(x, y_approx_S3, label=f'Approximation $S_3(x)$', linestyle='-.')  
  
    # 图表装饰  
    plt.legend()  
    plt.title('Comparison of $e^x$ with Legendre Polynomial Approximations')  
    plt.xlabel('x')  
    plt.ylabel('y')  
    plt.grid(True)  
  
    # 显示图表  
    plt.show()  
  
# 调用主函数  
if __name__ == "__main__":  
    main()