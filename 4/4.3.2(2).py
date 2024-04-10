import numpy as np
import matplotlib.pyplot as plt
from scipy.special import roots_legendre
from scipy.integrate import quad

def f(x):
    return np.exp(x)

def legendre_poly(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2*n - 1) * x * legendre_poly(n-1, x) - (n - 1) * legendre_poly(n-2, x)) / n

def legendre_coefficients_direct(n, f):
    n=n+1
    coefficients = []
    for k in range(n):
        integral, _ = quad(lambda x: f(x) * legendre_poly(k, x), -1, 1)
        coefficients.append((2*k + 1) / 2 * integral)
    return coefficients

def best_square_approximation(n, f):
    coefficients = legendre_coefficients_direct(n, f)
    n=n+1
    def S(x):
        result = 0
        for i in range(n):
            result += coefficients[i] * legendre_poly(i, x)
        return result
    return S

# 计算S1(x)和S3(x)
S1 = best_square_approximation(1, f)
S3 = best_square_approximation(3, f)

# 打印系数
print("Coefficients for S1(x):", legendre_coefficients_direct(1, f))
print("Coefficients for S3(x):", legendre_coefficients_direct(3, f))

# 绘制对比图像
x_values = np.linspace(-1, 1, 1000)
plt.plot(x_values, f(x_values), label='f(x)=exp(x)')
plt.plot(x_values, S1(x_values), label='S1(x)')
plt.plot(x_values, S3(x_values), label='S3(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of f(x) and its best square approximations')
plt.show()
