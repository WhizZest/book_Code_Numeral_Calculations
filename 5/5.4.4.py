import numpy as np  
from scipy.special import roots_laguerre  
from scipy.integrate import quad  
  
# 原始函数  
def f(x):  
    return 1 / (1 + x**3)  
  
# 使用高斯-拉盖尔公式计算积分  
def gauss_laguerre_integration(n, a=2):  
    x, w = roots_laguerre(n)  # 获取拉盖尔多项式的根和权重  
    integral = 0  
    for xi, wi in zip(x, w):  
        # 注意我们进行了变量替换 x -> x + a，这里x是拉盖尔多项式的根  
        integral += wi * f(xi + a) * np.exp(xi)  
    return integral  
  
# 使用高斯-拉盖尔公式计算积分的近似值  
n_points = 5  # 使用20个点的高斯-拉盖尔积分  
approx_integral = gauss_laguerre_integration(n_points)  
print(f"高斯-拉盖尔公式计算的积分值: {approx_integral}")  
  
# 使用SciPy的quad函数计算从2到无穷大的实际积分值  
# 由于我们的被积函数从2开始，我们不需要额外的变换函数  
actual_integral, error = quad(f, 2, np.inf)  
print(f"实际积分值: {actual_integral}")  
  
# 计算误差  
error_value = abs(approx_integral - actual_integral)  
print(f"误差: {error_value}")