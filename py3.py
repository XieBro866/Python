import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['PingFang SC', 'STHeiti Light', 'SimHei', 'Arial Unicode MS']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

# 创建数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(x/10)

# 创建画布和子图
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Matplotlib 多种图表示例', fontsize=16)

# 1. 折线图
axes[0, 0].plot(x, y1, 'b-', label='sin(x)', linewidth=2)
axes[0, 0].plot(x, y2, 'r--', label='cos(x)', linewidth=2)
axes[0, 0].set_title('折线图')
axes[0, 0].set_xlabel('X轴')
axes[0, 0].set_ylabel('Y轴')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# 2. 散点图
x_scatter = np.random.normal(5, 1.5, 100)
y_scatter = np.random.normal(5, 1.5, 100)
colors = np.random.rand(100)
sizes = 100 * np.random.rand(100)

axes[0, 1].scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.6, cmap='viridis')
axes[0, 1].set_title('散点图')
axes[0, 1].set_xlabel('X值')
axes[0, 1].set_ylabel('Y值')
axes[0, 1].grid(True, alpha=0.3)

# 3. 柱状图
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 33]
error = [2, 3, 4, 1, 2]

axes[1, 0].bar(categories, values, yerr=error, capsize=5, color=['#FF9999', '#66B2FF', '#99FF99', '#FFD700', '#FF69B4'])
axes[1, 0].set_title('柱状图')
axes[1, 0].set_xlabel('类别')
axes[1, 0].set_ylabel('数值')

# 4. 饼图
sizes_pie = [15, 30, 45, 10]
labels_pie = ['Python', 'Java', 'C++', '其他']
colors_pie = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

axes[1, 1].pie(sizes_pie, labels=labels_pie, colors=colors_pie, autopct='%1.1f%%', startangle=90)
axes[1, 1].set_title('编程语言占比')

# 调整布局
plt.tight_layout()
plt.show()

# 单独创建一个曲线图
plt.figure(figsize=(10, 6))
plt.plot(x, y3, 'g-', linewidth=2, label='e^(x/10)')
plt.fill_between(x, y3, alpha=0.2, color='green')
plt.title('指数函数曲线')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 3D 曲面图示例（如果需要3D功能）
try:
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    X = np.linspace(-5, 5, 50)
    Y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(X, Y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.set_title('3D 曲面图')
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_zlabel('Z轴')
    fig.colorbar(surf)
    plt.show()
except ImportError:
    print("3D 绘图需要额外的依赖库")