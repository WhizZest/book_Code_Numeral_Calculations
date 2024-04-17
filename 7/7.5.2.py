def newton_method_sqrt(a, guess, tolerance=1e-8, max_iterations=1000):
    """
    牛顿法求解 sqrt(a)
    
    参数：
    a: float，待求平方根的数，必须大于0
    guess: float，初始猜测值
    tolerance: float，允许的误差范围
    max_iterations: int，最大迭代次数
    
    返回：
    root: float，a的平方根
    iterations: int，迭代次数
    """
    if a <= 0:
        raise ValueError("a必须是一个大于0的常数")

    def f(x):
        return x ** 2 - a

    def f_prime(x):
        return 2 * x

    x = guess
    iterations = 0
    while True:
        iterations += 1
        x_new = x - f(x) / f_prime(x)
        if abs(x_new - x) < tolerance or iterations >= max_iterations:
            break
        x = x_new
    return x, iterations

# 待求平方根的数
a = 2

# 初始猜测值
initial_guess = a / 2

# 调用牛顿法函数
root, iterations = newton_method_sqrt(a, initial_guess)

print("sqrt({}) 的近似值:".format(a), root)
print("迭代次数:", iterations)
