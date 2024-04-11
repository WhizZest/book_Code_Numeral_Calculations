import numpy as np

def legendre_polynomial(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * legendre_polynomial(n - 1, x) - (n - 1) * legendre_polynomial(n - 2, x)) / n

def tridiagonal_legendre_matrix(n):
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if abs(i - j) == 1:
                matrix[i, j] = np.sqrt((2*j+1)*(2*i+1)/2) if i > j else np.sqrt((2*i+1)*(2*j+1)/2)
    return matrix

n = 5  # 生成5阶的勒让德多项式对应的三对角矩阵
matrix = tridiagonal_legendre_matrix(n)
print("Tridiagonal Legendre Matrix:")
print(matrix)

print("\nLegendre Polynomials:")
x_values = np.linspace(-1, 1, 100)
for i in range(n):
    legendre_values = [legendre_polynomial(i, x) for x in x_values]
    print(f"n={i}: {legendre_values}")
