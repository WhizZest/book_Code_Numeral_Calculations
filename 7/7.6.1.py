def f(x):  
    return x**3 + x**2 - 1  
  
def df(x):  
    return 3*x**2 + 2*x  
  
def newton_method(x0, tolerance=1e-6, max_iterations=100):  
    x = x0  
    for i in range(max_iterations):  
        fx = f(x)  
        if abs(fx) < tolerance:  
            print(f"Newton's method converged after {i} iterations. Solution: {x}")  
            return x  
        dfx = df(x)  
        if dfx == 0:  
            print("Zero derivative. No solution found.")  
            return None  
        x -= fx / dfx  
    print("Newton's method did not converge.")  
    return None  
  
def newton_descent_method(x0, tolerance=1e-6, max_iterations=100, lambda_=1.0, rho=0.5):  
    x = x0  
    for i in range(max_iterations):  
        fx = f(x)  
        if abs(fx) < tolerance:  
            print(f"Newton's descent method converged after {i} iterations. Solution: {x}")  
            return x  
        dfx = df(x)  
        if dfx == 0:  
            print("Zero derivative. No solution found.")  
            return None  
        x_new = x  
        while True:  
            delta_x = -lambda_ * fx / dfx  
            x_new = x + delta_x  
            if f(x_new) < fx:  
                break  
            lambda_ *= rho  
            if lambda_ < tolerance:  
                print("Step size became too small, stopping iterations.")  
                return None  
        x = x_new  
        lambda_ = 1.0  # Reset lambda for the next iteration  
    print("Newton's descent method did not converge.")  
    return None  
  
def secant_method(x0, x1, tolerance=1e-6, max_iterations=100):  
    for i in range(max_iterations):  
        fx0 = f(x0)  
        fx1 = f(x1)  
        if abs(fx1) < tolerance:  
            print(f"Secant method converged after {i} iterations. Solution: {x1}")  
            return x1  
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)  
        x0, x1 = x1, x2  
    print("Secant method did not converge.")  
    return None  
  
# 调用方法求解  
initial_guess_newton = 1.0  
solution_newton = newton_method(initial_guess_newton)  
  
initial_guess_newton_descent = 1.0  
solution_newton_descent = newton_descent_method(initial_guess_newton_descent)  
  
initial_guess_secant_1 = 0.0  
initial_guess_secant_2 = 2.0  
solution_secant = secant_method(initial_guess_secant_1, initial_guess_secant_2)