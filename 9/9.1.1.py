import numpy as np
from tabulate import tabulate
from scipy.integrate import solve_ivp

# 定义欧拉公式求解器
def euler_method(f, y0, x_start, x_end, h):
    x_values = np.arange(x_start, x_end + h, h)
    y_values = np.zeros_like(x_values)
    y_values[0] = y0

    for i in range(len(x_values) - 1):
        y_new = y_values[i] + h * f(x_values[i], y_values[i])
        y_values[i + 1] = y_new

    return x_values, y_values

# 定义微分方程dy/dx = y - 2x/y
def dy_dx(x, y):
    return y - 2 * x / y

# 初始条件
y0 = 1
x_start, x_end = 0, 1
h = 0.1

# 使用欧拉方法求解
x_values, y_values_euler = euler_method(dy_dx, y0, x_start, x_end, h)

# 计算精确解y(xn)对应的函数值（此处假设已知精确解函数y(x)）
def exact_solution(x):
    return (1 + 2*x)**0.5

# 如果无法提供精确解函数，可以使用更精确的数值方法（如四阶龙格-库塔法）作为近似参考
sol = solve_ivp(dy_dx, (x_start, x_end), [y0], t_eval=x_values, method='RK45')
y_values_exact = exact_solution(x_values)#sol.y[0]

# 计算误差 |yn - y(xn)|
error_values = np.abs(y_values_euler - y_values_exact)

# 使用字符串格式化确保每列至少显示4位小数
x_values_str = ['{:.1f}'.format(v) for v in x_values]
y_values_euler_str = ['{:.4f}'.format(v) for v in y_values_euler]
y_values_exact_str = ['{:.4f}'.format(v) for v in y_values_exact]
error_values_str = ['{:.4f}'.format(v) for v in error_values]

# 组合数据并绘制表格
data = np.column_stack((x_values_str, y_values_euler_str, y_values_exact_str, error_values_str))
headers = ['xn', 'yn', 'y(xn)', '|yn - y(xn)|']
print(tabulate(data, headers=headers, tablefmt='pretty'))