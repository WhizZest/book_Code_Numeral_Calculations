import numpy as np
import matplotlib.pyplot as plt

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
    
    return x_values, y_values

def f(x, y):
    return y - 2*x/y

def exact_solution(x):
    return (1 + 2*x)**0.5

# Parameters
x0 = 0
y0 = 1
h = 0.1
x_end = 1

# Solve using RK4 method
x_values, y_values = runge_kutta_4(f, x0, y0, h, x_end)

# Calculate exact solution
exact_values = exact_solution(x_values)

# Calculate absolute error
abs_error = np.abs(y_values - exact_values)

# Display results in a table with scientific notation for absolute error
print("x_n\t\ty_n\t\tExact\t\t|y_n - Exact| (scientific notation)")
for i in range(len(x_values)):
    print("{:.1f}\t\t{:.6f}\t{:.6f}\t{:.5e}".format(x_values[i], y_values[i], exact_values[i], abs_error[i]))

# Plot the results
plt.plot(x_values, y_values, label='Numerical Solution')
plt.plot(x_values, exact_values, label='Exact Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Numerical and Exact Solutions using RK4 Method')
plt.legend()
plt.grid(True)
plt.show()
