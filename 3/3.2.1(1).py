from scipy.interpolate import lagrange

# 已知点
x_known = [10, 11, 12, 13, 14]
y_known = [2.3026, 2.3979, 2.4849, 2.5649, 2.6391]

# 使用拉格朗日插值计算多项式
poly = lagrange(x_known, y_known)

# 计算 ln(11.75) 的近似值
x = 11.75
y_approx = poly(x)

print("使用拉格朗日插值得到的 ln(11.75) 的近似值为:", y_approx)

# 线性插值
x_linear = [11, 12]
y_linear = [2.3979, 2.4849]

# 使用线性插值计算多项式
poly = lagrange(x_linear, y_linear)

# 计算 ln(11.75) 的近似值
x = 11.75
y_approx_linear = poly(x)

print("使用线性插值得到的 ln(11.75) 的近似值为:", y_approx_linear)

# 抛物线插值
x_parabola = [11, 12, 13]
y_parabola = [2.3979, 2.4849, 2.5649]

# 使用抛物线插值计算多项式
poly = lagrange(x_parabola, y_parabola)

# 计算 ln(11.75) 的近似值
x = 11.75
y_approx_parabola = poly(x)

print("使用抛物线插值得到的 ln(11.75) 的近似值为:", y_approx_parabola)
