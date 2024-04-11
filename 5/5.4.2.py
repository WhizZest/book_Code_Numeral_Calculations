import numpy as np
import matplotlib.pyplot as plt
from scipy.special import roots_legendre
from scipy import integrate

def f(x, alpha):
    return np.abs(x)**(alpha + 3/5)

def gauss_legendre(f, alpha, n):
    x, w = roots_legendre(n)
    integral = sum(w[i] * f(x[i], alpha) for i in range(n))
    return integral

alphas = [0, 1, 2]  # 不同的 alpha 值
n_values = np.arange(1, 101)  # n 的值范围从 1 到 100

# 计算高斯–勒让德积分结果和误差
gauss_integrals = {alpha: [gauss_legendre(f, alpha, n) for n in n_values] for alpha in alphas}
actual_integrals = {alpha: [integrate.quad(lambda x: f(x, alpha), -1, 1)[0] for _ in n_values] for alpha in alphas}
errors = {alpha: np.abs(np.array(gauss_integrals[alpha]) - np.array(actual_integrals[alpha])) for alpha in alphas}

# 绘制图像
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
for alpha in alphas:
    plt.plot(n_values, gauss_integrals[alpha], label=f'alpha={alpha}')
plt.xlabel('log(n)')
plt.ylabel('log(Gauss Legendre Integral)')
plt.title('Gauss Legendre Integral vs log(n)')
plt.legend()
plt.xscale('log')
plt.yscale('log')

plt.subplot(1, 2, 2)
for alpha in alphas:
    plt.plot(n_values, errors[alpha], label=f'alpha={alpha}')
plt.xlabel('log(n)')
plt.ylabel('log(Error)')
plt.title('Error vs log(n)')
plt.legend()
plt.xscale('log')
plt.yscale('log')

plt.tight_layout()
plt.show()
