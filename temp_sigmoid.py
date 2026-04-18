import numpy as np
import matplotlib.pyplot as plt


# 定义 Sigmoid 激活函数
# 公式：f(x) = 1 / (1 + e^(-x))
# 特点：将任意实数映射到 (0, 1) 区间，常用于二分类问题的输出层
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# 生成 100 个随机整数，范围在 [-10, 10)
x = np.random.randint(-10, 10, 100)

# 对 x 进行排序，使绘制的曲线更平滑连续
x.sort()

# 计算每个 x 对应的 sigmoid 值
y = sigmoid(x)

# 绘制 sigmoid 函数曲线
plt.plot(x, y)
plt.show()
