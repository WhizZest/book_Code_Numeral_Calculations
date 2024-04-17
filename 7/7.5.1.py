import math  
  
def f(x):  
    return x - math.cos(x)  
  
def df(x):  
    return 1 + math.sin(x)  
  
def newton_method(x0, tolerance=1e-15, max_iterations=100):  
    x = x0  
    for i in range(max_iterations):  
        fx = f(x)  
        if abs(fx) < tolerance:  
            print(f"Found solution after {i} iterations.")  
            return x  
        dfx = df(x)  
        if dfx == 0:  
            print("Zero derivative. No solution found.")  
            return None  
        x = x - fx/dfx  
    print("Exceeded maximum iterations. No solution found.")  
    return None  
  
# 选择一个初始点，例如 x0 = 1.0  
x0 = 1.0  
solution = newton_method(x0)  
if solution is not None:  
    print(f"The solution is x = {solution}")