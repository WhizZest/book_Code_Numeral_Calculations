import numpy as np

def f(x):
    return np.sin(x) / x if x != 0 else 1

def romberg_integration(f, a, b, tol=1e-7):
    R = np.zeros((2, 2))
    n = 1
    R[0, 0] = 0.5 * (b - a) * (f(a) + f(b))
    print("第 0 次迭代：", R[0, 0])
    for i in range(1, 21):
        h = (b - a) / n
        sum_f = sum(f(a + (k + 0.5) * h) for k in range(n))
        R[1, 0] = 0.5 * R[0, 0] + 0.5 * h * sum_f
        print("第", i, "次迭代：", R[1, 0], end="")
        for m in range(1, i + 1):
            R[1, m] = R[1, m-1] + (R[1, m-1] - R[0, m-1]) / ((4**m) - 1)
            print(", ", R[1, m], end="")
        print()
        if i > 0 and abs(R[1, i] - R[0, i-1]) < tol:
            return R[1, i], i
        n *= 2
        R[0, :] = R[1, :]
        R = np.resize(R, (2, i+2))
    print("达到最大迭代次数仍未满足精度要求")

integral, iterations = romberg_integration(f, 0, 1)
print("积分值:", integral)
print("迭代次数:", iterations)
