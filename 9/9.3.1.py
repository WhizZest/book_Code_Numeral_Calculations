import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, x0, y0, h, x_end):
    # Initialize arrays to store the solution
    num_steps = round((x_end - x0) / h) + 1
    x_values = np.linspace(x0, x_end, num_steps)
    y_values = np.zeros(num_steps)
    y_values[0] = y0
    
    # Apply Euler's method
    for i in range(1, num_steps):
        y_values[i] = y_values[i-1] + h * f(x_values[i-1], y_values[i-1])
    
    return y_values[-1]

def improved_euler_method(f, x0, y0, h, x_end):
    # Initialize arrays to store the solution
    num_steps = round((x_end - x0) / h) + 1
    x_values = np.linspace(x0, x_end, num_steps)
    y_values = np.zeros(num_steps)
    y_values[0] = y0
    
    # Apply improved Euler's method (Trapezoidal method)
    for i in range(1, num_steps):
        y = y_values[i-1] + 0.5 * h * (f(x_values[i-1], y_values[i-1]) + f(x_values[i], y_values[i-1] + h*f(x_values[i-1], y_values[i-1])))
        y_values[i] = y
    
    return y_values[-1]

def trapezoidal_method(f, x0, y0, h, x_end):
    # Initialize arrays to store the solution
    num_steps = round((x_end - x0) / h) + 1
    x_values = np.linspace(x0, x_end, num_steps)
    y_values = np.zeros(num_steps)
    y_values[0] = y0
    
    # Apply Trapezoidal method
    for i in range(1, num_steps):
        y = y_values[i-1]
        for _ in range(5):  # 迭代求解
            y_next = y_values[i-1] + 0.5 * h * (f(x_values[i-1], y_values[i-1]) + f(x_values[i], y))
            if np.abs(y_next - y) < 1e-10:  # 当迭代精度满足要求时停止迭代
                break
            y = y_next
        y_values[i] = y
    
    return y_values[-1]

def runge_kutta_4(f, x0, y0, h, x_end):
    # Initialize arrays to store the solution
    num_steps = round((x_end - x0) / h) + 1
    x_values = np.linspace(x0, x_end, num_steps)
    y_values = np.zeros(num_steps)
    y_values[0] = y0
    
    # Apply RK4 method
    for i in range(1, num_steps):
        k1 = h * f(x_values[i-1], y_values[i-1])
        k2 = h * f(x_values[i-1] + 0.5 * h, y_values[i-1] + 0.5 * k1)
        k3 = h * f(x_values[i-1] + 0.5 * h, y_values[i-1] + 0.5 * k2)
        k4 = h * f(x_values[i-1] + h, y_values[i-1] + k3)
        
        y_values[i] = y_values[i-1] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    
    return y_values[-1]

def f(x, y):
    return y - 2*x/y

def exact_solution(x):
    return (1 + 2*x)**0.5

def calculate_error(method, N):
    h = 1/N
    x_end = 1
    exact_result = exact_solution(x_end)
    numerical_result = method(f, x0, y0, h, x_end)
    error = np.abs(numerical_result - exact_result)
    return error

# Initialize k values
k_values = [0, 1, 2, 3, 4, 5]

# Parameters
x0 = 0
y0 = 1
exact_result = exact_solution(1)
errors = []

# Calculate errors for each method and each k value
for k in k_values:
    N = 20 * 2**k
    euler_error = calculate_error(euler_method, N)
    improved_euler_error = calculate_error(improved_euler_method, N)
    trapezoidal_error = calculate_error(trapezoidal_method, N)
    rk4_error = calculate_error(runge_kutta_4, N)
    errors.append([k, euler_error, improved_euler_error, trapezoidal_error, rk4_error])

# Display errors in a table
print("k\tEuler\t\tImproved Euler\tTrapezoidal\tRK4")
for error_row in errors:
    print("{}\t{:.2e}\t{:.2e}\t{:.2e}\t{:.2e}".format(*error_row))

# Plot the results
methods = ['Euler', 'Improved Euler', 'Trapezoidal', 'RK4']
plt.figure(figsize=(10, 6))
for i in range(1, 5):
    plt.plot(k_values, [row[i] for row in errors], label=methods[i-1])
plt.xlabel('k')
plt.ylabel('Absolute Error at x=1')
plt.title('Absolute Error at x=1 for Different Methods')
plt.yscale('log')
plt.xticks(k_values)
plt.legend()
plt.grid(True)
plt.show()
