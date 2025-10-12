import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义复变函数 w = sin(z)
def f(z):
    return np.sin(z)

# 生成以原点为圆心，半径为 2 的圆盘
radius = 2
x = np.linspace(-radius, radius, 200)  # x 方向的点
y = np.linspace(-radius, radius, 200)  # y 方向的点
X, Y = np.meshgrid(x, y)  # 生成网格点
Z = X + 1j * Y  # 将网格点转换为复数形式

# 筛选出圆盘内的点
mask = np.sqrt(X**2 + Y**2) <= radius
Z = Z[mask]  # 只保留圆盘内的点

# 计算 w = sin(z)
W = f(Z)

# 绘制 3D 图像
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制 z 的圆盘，z 的实部和虚部作为 x 和 y，w 的实部作为 z
sc = ax.scatter(Z.real, Z.imag, W.real, c=W.imag, cmap='viridis', s=5, label="w = sin(z)")

# 添加颜色条，表示 w 的虚部
cbar = plt.colorbar(sc, ax=ax, shrink=0.5, aspect=10)
cbar.set_label("Im(w)")

# 设置坐标轴标签
ax.set_xlabel("Re(z)")
ax.set_ylabel("Im(z)")
ax.set_zlabel("Re(w)")

# 设置标题和图例
ax.set_title("复变函数 w = sin(z) 的 3D 图像")
ax.legend()

# 显示图像
plt.show()