import math  
  
# 定义函数f(x)  
def f(x):  
    return x**2 + math.sin(10*x) - 1  
  
# 定义函数f(x)的导数f'(x)  
def df(x):  
    return 2*x + 10*math.cos(10*x)  
  
# 牛顿下山法  
def newton_raphson_with_damping(x0, tolerance=1e-10, max_iterations=100, lambda_start=1.0, lambda_decrease_factor=0.5):  
    x = x0  
    lambda_value = lambda_start  
      
    for iteration in range(max_iterations):  
        fx = f(x)  
        dfx = df(x)  
          
        # 使用牛顿法公式计算下一个迭代点，但加入了下山因子  
        x_new = x - lambda_value * fx / dfx  
        fx_new = f(x_new)  
          
        # 如果下山方向没有使得函数值下降，则减小下山因子  
        while abs(fx_new) >= abs(fx):  
            lambda_value *= lambda_decrease_factor  
            x_new = x - lambda_value * fx / dfx  
            fx_new = f(x_new)  
            if lambda_value < tolerance:  
                print("Lambda became too small, stopping iterations.")  
                return None  
          
        # 打印每次迭代的λ和x值  
        print(f"Iteration {iteration+1}: λ={lambda_value}, x={x_new}")  
          
        # 检查收敛性  
        if abs(fx_new) < tolerance:  
            print(f"Converged after {iteration+1} iterations. Solution: x = {x_new}")  
            return x_new  
          
        x = x_new  
        fx = fx_new  
        lambda_value = lambda_start  # 重置下山因子  
          
    print("Maximum iterations reached before convergence.")  
    return x  
  
# 初始点选择  
x0 = 30.0  
# 调用牛顿下山法函数  
solution = newton_raphson_with_damping(x0)