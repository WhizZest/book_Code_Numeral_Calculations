def f(x):  
    return x**3 - x - 1  
  
def bisection_method(a, b, tol=1e-6, max_iter=100):  
    if f(a) * f(b) >= 0:  
        print("f(a) and f(b) must have different signs.")  
        return None  
      
    iter_count = 0  
    c = a  
    while ((b - a) / 2 >= tol) and (iter_count < max_iter):  
        iter_count += 1  
        c = (a + b) / 2  
        print(f"Iteration {iter_count}: c = {c}, f(c) = {f(c)}")  
          
        if f(c) == 0.0:  
            break  
        elif f(c) * f(a) < 0:  
            b = c  
        else:  
            a = c  
              
    return c  
  
# 选择合适的初始区间 [a, b]  
a = 1.0  
b = 2.0  
root = bisection_method(a, b)  
if root is not None:  
    print("\nThe root is:", root)  
else:  
    print("Failed to find a root in the given interval.")