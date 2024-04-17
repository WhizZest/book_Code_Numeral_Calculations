iterations = 0
def fixed_point_iteration(func, initial_guess, tol=1e-6, max_iter=1000, divergence_threshold=1e6):  
    global iterations
    x = initial_guess  
    iterations = 0
    for i in range(max_iter):  
        iterations += 1
        try:  
            x_new = func(x)  
        except ZeroDivisionError:  
            print("Error: Division by zero occurred. Aborting iteration.")  
            return None  
  
        if abs(x_new - x) > divergence_threshold:  
            print("Warning: Iteration may be diverging. Aborting iteration.")  
            return None  
  
        if abs(x_new - x) < tol:  
            return x_new, i + 1  
  
        x = x_new  
  
    print("Warning: Maximum iterations reached without convergence.")  
    return x, max_iter  
  
# 四种不动点迭代函数  
def fixed_point1(x):  
    return x ** 3 - 1  
  
def fixed_point2(x):  
    return (x + 1) ** (1 / 3)  
  
def fixed_point3(x):  
    if x**2 - 1 == 0:  
        raise ZeroDivisionError  # 防止分母为零  
    return 1 / (x ** 2 - 1)  
  
def fixed_point4(x):  
    if 3 * x ** 2 - 1 == 0:  
        raise ZeroDivisionError  # 防止分母为零  
    return x - (x ** 3 - x - 1) / (3 * x ** 2 - 1)  
  
# 初始猜测值  
initial_guess = 1.5  
  
# 定义一个包含所有不动点迭代函数的列表  
fixed_point_functions = [fixed_point1, fixed_point2, fixed_point3, fixed_point4]  
  
# 使用for循环遍历并执行每个不动点迭代函数  
for i, func in enumerate(fixed_point_functions, start=1):  
    try:  
        root,_ = fixed_point_iteration(func, initial_guess)  
        if root is not None:  
            print(f"Root for ({i}): {root}, Iterations: {iterations}")  
    except Exception as e:  
        print(f"An error occurred during function ({i}): {e}, Iterations: {iterations}")  