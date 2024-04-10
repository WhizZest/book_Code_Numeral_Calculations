import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# 给定记录
fj = np.array([2, 1, 0, 1])

# 计算离散傅里叶变换
Cj = fft(fj)
print("离散谱 Cj:", Cj)

# 计算频率轴上的频率值
N = len(fj)
dt = 1  # 假设采样间隔为1
freq = np.fft.fftfreq(N, d=dt)

# 绘制图像
plt.figure(figsize=(10, 8))

# 绘制fj的图像
plt.subplot(2, 1, 1)
plt.stem(np.arange(len(fj)), fj, markerfmt='ro', basefmt='k-')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Original Data')

# 绘制离散谱的图像
plt.subplot(2, 1, 2)
plt.stem(freq, np.abs(Cj), markerfmt='ro', basefmt='k-')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Discrete Spectrum')

plt.tight_layout()
plt.show()
