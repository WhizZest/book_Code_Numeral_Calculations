import numpy as np
  
def homotopy_single_equation(f, x0, t_steps=100, tol=1e-6):  
    def homotopy_function(x, t):  
        return (1 - t) * (x - x0) + t * f(x)  
  
    x = x0  
    for t in np.linspace(0, 1, t_steps):  
        while True:  
            fx = homotopy_function(x, t)  
            if abs(fx) < tol:  
                break  
            derivative = (homotopy_function(x + tol, t) - homotopy_function(x, t)) / tol  
            x = x - fx / derivative  
    return x  
  
# 使用示例  
f = lambda x: x**3 + x - 6  
x0 = 1  
root = homotopy_single_equation(f, x0)  
print(f"The root of the equation is: {root}")
  
def homotopy_equation_system(F, x0, t_steps=100, tol=1e-6):  
    def G(x):
        return np.array(x) - np.array(x0)
    
    def homotopy_system(x, t):  
        return (1 - t) * G(x) + t * np.array(F(x)) 

    def gradient_F(x):  
        return np.array([[1, -np.sin(x[1])], [np.cos(x[0]), 1]])
    
    def gradient_h_t(x, t):  
        # 关于t的偏导数  
        return F(x) - G(x) 
  
    def jacobian(x, t):  
        J = np.zeros((len(x), len(x)))  
        h = 1e-7  # A small perturbation for numerical differentiation  
        for i in range(len(x)):  
            temp_x = x.copy()  
            temp_x[i] += h  
            J[:, i] = (homotopy_system(temp_x, t) - homotopy_system(x, t)) / h  
        return J  
    def jacobian_2(x, t):
        return t*gradient_F(x) + (1 - t)*np.eye(len(x))
  
    x = np.array(x0, dtype=float)  # 确保x是浮点数类型  
    # 生成从dt到1，间隔是dt的t序列
    dt = 0.01
    sequence = np.arange(dt, 1 + dt, dt)
    for t in sequence:
        J = jacobian(x, t - dt)  
        x = x - dt * np.linalg.solve(J, gradient_h_t(x, t - dt))
        Fx = homotopy_system(x, t)
        J = jacobian(x, t)
        delta_x = np.linalg.solve(J, -Fx)  
        x += delta_x
    return x  

# 简化版
def homotopy_equation_system_simplified(F, x0, t_steps=100, tol=1e-6):  
    def homotopy_system(x, t):  
        return (1 - t) * (np.array(x) - np.array(x0)) + t * np.array(F(x))  
  
    def jacobian(x, t):  
        J = np.zeros((len(x), len(x)))  
        h = 1e-7  # A small perturbation for numerical differentiation  
        for i in range(len(x)):  
            temp_x = x.copy()  
            temp_x[i] += h  
            J[:, i] = (homotopy_system(temp_x, t) - homotopy_system(x, t)) / h  
        return J  
  
    x = np.array(x0, dtype=float)  
    for t in np.linspace(0, 1, t_steps):  
        while True:  
            Fx = homotopy_system(x, t)  
            if np.linalg.norm(Fx) < tol:  
                break  
            J = jacobian(x, t)  
            delta_x = np.linalg.solve(J, -Fx)  
            x += delta_x  
    return x  
# 定义角度制方程组  
def equations_angles(x):  
    x1, x2 = x
    return [x1 + np.cos(x2 * np.pi / 180) - 1, -np.sin(x1 * np.pi / 180) + x2 - 1]  

# 定义弧度制（numpy默认使用弧度制）方程组  
def equations_degrees(x):  
    x1, x2 = x  
    return [x1 + np.cos(x2) - 1, -np.sin(x1) + x2 - 1] 
  
# 初始解  
x0_system = [-1, 1]  
# 三角函数为角度制
## 使用同伦算法求解方程组  
root_system = homotopy_equation_system(equations_angles, x0_system)  
print("When the equations are in angles:")
print(f"The roots of the equation system by homotopy method are: {root_system}")
result = equations_angles(root_system)
print(f"The results of the equation system are: {result}")
## 使用简化版同伦算法求解方程组
root_system = homotopy_equation_system_simplified(equations_angles, x0_system)
print(f"The roots of the equation system by simplified homotopy method are: {root_system}")
result = equations_angles(root_system)
print(f"The results of the equation system are: {result}")
print("When the equations are in degrees:")
# 三角函数为弧度制
## 使用同伦算法求解方程组 
root_system = homotopy_equation_system(equations_degrees, x0_system)
print(f"The roots of the equation system by homotopy method are: {root_system}")
result = equations_degrees(root_system)
print(f"The results of the equation system are: {result}")
ModelLength = np.linalg.norm(result)
print(f"The length of the model is: {ModelLength}")
## 使用简化版同伦算法求解方程组
root_system = homotopy_equation_system_simplified(equations_degrees, x0_system)
print(f"The roots of the equation system by simplified homotopy method are: {root_system}")
result = equations_degrees(root_system)
print(f"The results of the equation system are: {result}")
ModelLength = np.linalg.norm(result)
print(f"The length of the model is: {ModelLength}")
# 其他结果验证
result = equations_degrees([0.262119524902768, 0.740871739227832])
print(f"Other results of the equation system are: {result}")
ModelLength = np.linalg.norm(result)
print(f"The length of the model is: {ModelLength}")