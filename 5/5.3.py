import numpy as np

def f(x):
    return np.where(x != 0, np.sin(x) / x, 1)

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral = h * (np.sum(y) - 0.5 * (y[0] + y[-1]))
    return integral

def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("The number of intervals must be even for Simpson's rule.")
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral = h / 3 * (y[0] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]) + y[-1])
    return integral

def newton_cotes_integration(f, a, b, order):
    orders = {
        1: trapezoidal_rule,
        2: simpsons_rule,
        3: lambda f, a, b, n: (2 * trapezoidal_rule(f, a, b, n) + simpsons_rule(f, a, b, n)) / 3,
        4: lambda f, a, b, n: (3 * simpsons_rule(f, a, b, n) + trapezoidal_rule(f, a, b, n)) / 4,
        5: lambda f, a, b, n: (4 * simpsons_rule(f, a, b, n) + trapezoidal_rule(f, a, b, n)) / 5,
        6: lambda f, a, b, n: (5 * simpsons_rule(f, a, b, n) + 8 * trapezoidal_rule(f, a, b, n)) / 13,
        7: lambda f, a, b, n: (6 * simpsons_rule(f, a, b, n) + 18 * trapezoidal_rule(f, a, b, n) + 
                               9 * (trapezoidal_rule(f, a, b, n // 2) - simpsons_rule(f, a, b, n // 2))) / 19
    }
    if order not in orders:
        raise ValueError("Order must be between 1 and 7.")
    return orders[order](f, a, b, 1000)

for order in range(1, 8):
    integral = newton_cotes_integration(f, 0, 1, order)
    print(f"阶数 {order} 的积分值:", integral)
