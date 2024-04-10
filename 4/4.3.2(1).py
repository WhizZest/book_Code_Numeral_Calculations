import numpy as np  
from scipy.special import eval_legendre as P  
from scipy.integrate import quad  
  
def compute_coefficients_direct(f, N):  
    coefficients = []  
    for n in range(N + 1):  
        # 使用SciPy的quad函数进行数值积分  
        integral = quad(lambda x: f(x) * P(n, x), -1, 1)[0]  
        # 根据勒让德多项式的正交性计算系数  
        a_n = (2 * n + 1) / 2 * integral  
        coefficients.append(a_n)  
    return coefficients  
  
# 定义被逼近的函数，例如 f(x) = e^x  
def f(x):  
    return np.exp(x)  
  
# 计算逼近多项式的系数  
N = 1  # 例如，我们选择N=1来计算S1(x)的系数  
coefficients = compute_coefficients_direct(f, N)  
print("Coefficients for S{}(x): {}".format(N, coefficients))
N = 3  # 例如，我们选择N=3来计算S3(x)的系数  
coefficients = compute_coefficients_direct(f, N)  
print("Coefficients for S{}(x): {}".format(N, coefficients))