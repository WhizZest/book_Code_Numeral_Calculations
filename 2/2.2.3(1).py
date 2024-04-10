def thomas_algorithm(a, b, c, d, n):  
    # a, b, c 是三对角矩阵的下、主、上对角线的元素  
    # d 是等式右边的向量  
    # n 是方程组中方程的个数  
    # 初始化c'和d'  
    c_prime = [0 for _ in range(n)]  
    d_prime = [0 for _ in range(n)]  
      
    # 追赶法的第一步：消元，对三对角线方程组进行LU分解  
    c_prime[0] = c[0] / b[0]  
    d_prime[0] = d[0] / b[0]  
      
    for i in range(1, n-1):  
        temp = b[i] - a[i-1] * c_prime[i-1]  
        c_prime[i] = c[i] / temp  
        d_prime[i] = (d[i] - a[i-1] * d_prime[i-1]) / temp  
    i = n-1
    temp = b[i] - a[i-1] * c_prime[i-1]
    d_prime[i] = (d[i] - a[i-1] * d_prime[i-1]) / temp  
    # 追赶法的第二步：回代，从最后一个方程开始解  
    x = [0 for _ in range(n)]  
    x[n-1] = d_prime[n-1]  
      
    for i in range(n-2, -1, -1):  
        x[i] = d_prime[i] - c_prime[i] * x[i+1]  
      
    return x  
  
# 将线性系统的参数转化为三个列表a, b, c以及d  
a = [-1, -2, -3]  # 下对角线元素  
b = [2, 3, 4, 5]  # 主对角线元素  
c = [-1, -2, -3]  # 上对角线元素  
d = [6, 1, -2, 1]  # 方程右边的值  
n = len(b)  # 方程组中方程的个数  
  
# 调用函数求解  
solution = thomas_algorithm(a, b, c, d, n)  
  
# 输出结果  
print("解为：", solution)