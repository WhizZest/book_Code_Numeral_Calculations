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
    
    return y_values

def backward_euler_method(f, x0, y0, h, x_end):
    # Initialize arrays to store the solution
    num_steps = round((x_end - x0) / h) + 1
    x_values = np.linspace(x0, x_end, num_steps)
    y_values = np.zeros(num_steps)
    y_values[0] = y0
    
    # Apply backward Euler's method
    for i in range(1, num_steps):
        y_values[i] = y_values[i-1] / (1 + 100 * h)
    
    return y_values

def f(x, y):
    return -100 * y

def exact_solution(x_values):
    return np.exp(-100 * x_values)

# Parameters
x0 = 0
y0 = 1
h_values = [0.025, 0.005]
x_end = 0.3

# Initialize arrays to store results
y_values_euler = []
y_values_backward_euler = []
exact_values = []

# Calculate solutions for each step size
for h in h_values:
    x_values = np.linspace(x0, x_end, round((x_end - x0) / h) + 1)
    y_values_euler.append(euler_method(f, x0, y0, h, x_end))
    y_values_backward_euler.append(backward_euler_method(f, x0, y0, h, x_end))
    exact_values.append(exact_solution(x_values))

# Display errors in a table
print("Step Size h=0.025")
print("x\t\tEuler Error\t\tBackward Euler Error")
for i, x in enumerate(np.linspace(x0, x_end, len(y_values_euler[0]))):
    print("{:.3f}\t\t{:.6f}\t\t{:.6f}".format(x, np.abs(y_values_euler[0][i] - exact_values[0][i]), np.abs(y_values_backward_euler[0][i] - exact_values[0][i])))

print("\nStep Size h=0.005")
print("x\t\tEuler Error\t\tBackward Euler Error")
for i, x in enumerate(np.linspace(x0, x_end, len(y_values_euler[1]))):
    print("{:.3f}\t\t{:.6f}\t\t{:.6f}".format(x, np.abs(y_values_euler[1][i] - exact_values[1][i]), np.abs(y_values_backward_euler[1][i] - exact_values[1][i])))

# Plot the results
plt.figure(figsize=(10, 6))

# Plot numerical solutions
for i, h in enumerate(h_values):
    plt.subplot(2, 1, i + 1)
    plt.plot(np.linspace(x0, x_end, len(y_values_euler[i])), y_values_euler[i], label=f'Euler Method (h={h})')
    plt.plot(np.linspace(x0, x_end, len(y_values_backward_euler[i])), y_values_backward_euler[i], label=f'Backward Euler Method (h={h})')
    plt.plot(np.linspace(x0, x_end, len(exact_values[i])), exact_values[i], label='Exact Solution')
    plt.title(f'Numerical Solutions with h={h}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()
