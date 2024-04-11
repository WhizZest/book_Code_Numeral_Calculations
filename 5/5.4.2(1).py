import numpy as np
from scipy.special import roots_legendre
from scipy import integrate

def f(x, alpha):
    return np.abs(x)**(alpha + 3/5)

def gauss_legendre(f, alpha, n):
    x, w = roots_legendre(n)
    integral = sum(w[i] * f(x[i], alpha) for i in range(n))
    return integral

alpha = 1  # 修改 alpha 的值
n = 100  # 修改高斯–勒让德公式的阶数
gauss_integral = gauss_legendre(f, alpha, n)
actual_integral, _ = integrate.quad(lambda x: f(x, alpha), -1, 1)
error = np.abs(gauss_integral - actual_integral)
print("高斯–勒让德积分结果:", gauss_integral)
print("实际积分结果:", actual_integral)
print("误差:", error)
