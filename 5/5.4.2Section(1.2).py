import numpy as np

def legendre_gauss_points_and_weights(n):
    # 使用numpy中的函数计算勒让德多项式对应的高斯点和高斯系数
    # 返回高斯点和高斯系数
    return np.polynomial.legendre.leggauss(n)

n = 5  # 生成5个高斯点及高斯系数
gauss_points, gauss_weights = legendre_gauss_points_and_weights(n)
print("Gaussian Points:", gauss_points)
print("Gaussian Weights:", gauss_weights)
