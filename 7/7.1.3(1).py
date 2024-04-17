import matplotlib.pyplot as plt

# 生成斐波那契序列的前 n 项
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def plot_sequence(sequence, label):
    plt.plot(range(1, len(sequence) + 1), sequence, label=label)

n = 20  # 可以根据需要调整项数

# 生成序列1的值
sequence_1 = [2**(1-k) for k in range(1, n+1)]
plot_sequence(sequence_1, "2^(1-k)")

# 生成序列2的值
sequence_2 = [0.9**(k-1) for k in range(1, n+1)]
plot_sequence(sequence_2, "0.9^(k-1)")

# 生成序列3的值
fib_sequence = fibonacci(n+2)  # 确保斐波那契序列足够长
sequence_3 = [2**(1-fib_sequence[k+1]) for k in range(1, n+1)]
plot_sequence(sequence_3, "2^(1-F_(k+1))")

# 生成序列4的值
sequence_4 = [2**(2-2**k) for k in range(1, n+1)]
plot_sequence(sequence_4, "2^(2-2^k)")

plt.xlabel("k")
plt.ylabel("Sequence Value")
plt.title("Sequences with respect to k")
plt.legend()
plt.grid(True)
plt.show()
