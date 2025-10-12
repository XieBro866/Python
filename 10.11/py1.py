import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义复变函数 w = sin(z)
def f(z):
    return np.sin(z)

# 生成以原点为圆心，半径为 2 的圆盘
radius = 2
x = np.linspace(-radius, radius, 100)  # 减少网格点数量
y = np.linspace(-radius, radius, 100)
X, Y = np.meshgrid(x, y)  # 生成网格点
Z = X + 1j * Y  # 将网格点转换为复数形式

# 筛选出圆盘内的点
mask = np.sqrt(X**2 + Y**2) <= radius
Z[~mask] = np.nan  # 将圆盘外的点设置为 NaN

# 计算 w = sin(z)
W = f(Z)

# 绘制 3D 曲面图
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制曲面图，X 和 Y 为网格点，W.real 为 Z 轴高度，W.imag 为颜色
surf = ax.plot_surface(
    X, Y, W.real,
    cmap='viridis',  # 使用简单的颜色映射
    rstride=5, cstride=5,  # 增大步长以减少绘制密度
    edgecolor='none'  # 去掉网格线
)

# 添加颜色条，表示 w 的虚部
cbar = plt.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
cbar.set_label("Im(w)")

# 设置坐标轴标签
ax.set_xlabel("Re(z)")
ax.set_ylabel("Im(z)")
ax.set_zlabel("Re(w)")

# 设置标题
ax.set_title("复变函数 w = sin(z) 的 3D 曲面图（优化性能）")

# 显示图像
plt.show()