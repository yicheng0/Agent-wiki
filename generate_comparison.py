import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 创建画布
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# 背景色
fig.patch.set_facecolor('#FFF8E7')
ax.set_facecolor('#FFF8E7')

# 标题
ax.text(7, 9.3, '前向传播 vs 反向传播 (核心对比)',
        fontsize=24, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFE4B5', edgecolor='#FF8C00', linewidth=2))

# 中间分隔线
ax.plot([7, 7], [0.5, 8.5], 'k-', linewidth=3, zorder=1)
ax.text(7, 8.7, '知识对比', fontsize=14, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFD700', edgecolor='black'))

# ========== 左侧：前向传播 ==========
ax.text(3.5, 8.2, '前向传播', fontsize=20, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#87CEEB', edgecolor='#4682B4', linewidth=2))
ax.text(3.5, 7.8, 'Forward Propagation', fontsize=11, ha='center', style='italic', color='#4682B4')

# 第1行：方向
y_pos = 7.0
ax.add_patch(FancyBboxPatch((1.2, y_pos-0.3), 4.6, 0.6,
                            boxstyle='round,pad=0.1', facecolor='#E0F7FA', edgecolor='#00ACC1', linewidth=2))
ax.text(1.5, y_pos, '方向:', fontsize=12, fontweight='bold', va='center')
ax.text(3.5, y_pos, '输入 → 输出', fontsize=13, ha='center', va='center', color='#00695C')
# 箭头
ax.annotate('', xy=(5.3, y_pos), xytext=(2.3, y_pos),
            arrowprops=dict(arrowstyle='->', lw=3, color='#00ACC1'))

# 第2行：目的
y_pos = 6.0
ax.add_patch(FancyBboxPatch((1.2, y_pos-0.3), 4.6, 0.6,
                            boxstyle='round,pad=0.1', facecolor='#FFF9C4', edgecolor='#F57C00', linewidth=2))
ax.text(1.5, y_pos, '目的:', fontsize=12, fontweight='bold', va='center')
ax.text(3.5, y_pos, '计算预测值', fontsize=13, ha='center', va='center', color='#E65100')

# 第3行：计算内容
y_pos = 5.0
ax.add_patch(FancyBboxPatch((1.2, y_pos-0.3), 4.6, 0.6,
                            boxstyle='round,pad=0.1', facecolor='#E1BEE7', edgecolor='#8E24AA', linewidth=2))
ax.text(1.5, y_pos, '计算:', fontsize=12, fontweight='bold', va='center')
ax.text(3.5, y_pos, 'y = f(wx + b)', fontsize=13, ha='center', va='center',
        color='#4A148C', family='monospace', fontweight='bold')

# 第4行：特点
y_pos = 4.0
ax.add_patch(FancyBboxPatch((1.2, y_pos-0.3), 4.6, 0.6,
                            boxstyle='round,pad=0.1', facecolor='#C8E6C9', edgecolor='#388E3C', linewidth=2))
ax.text(1.5, y_pos, '特点:', fontsize=12, fontweight='bold', va='center')
ax.text(3.5, y_pos, '逐层传递数据', fontsize=13, ha='center', va='center', color='#1B5E20')

# 第5行：代码
y_pos = 2.8
ax.add_patch(FancyBboxPatch((1.2, y_pos-0.5), 4.6, 1.0,
                            boxstyle='round,pad=0.1', facecolor='#FFCCBC', edgecolor='#D84315', linewidth=2))
ax.text(1.5, y_pos+0.3, '代码:', fontsize=12, fontweight='bold', va='center')
ax.text(3.5, y_pos+0.15, 'outputs = model(x)', fontsize=11, ha='center', va='center',
        family='monospace', color='#BF360C')
ax.text(3.5, y_pos-0.15, 'loss = criterion(', fontsize=11, ha='center', va='center',
        family='monospace', color='#BF360C')
ax.text(3.5, y_pos-0.35, '    outputs, labels)', fontsize=11, ha='center', va='center',
        family='monospace', color='#BF360C')

# 第6行：结果
y_pos = 1.5
ax.add_patch(FancyBboxPatch((1.2, y_pos-0.3), 4.6, 0.6,
                            boxstyle='round,pad=0.1', facecolor='#B2DFDB', edgecolor='#00897B', linewidth=2))
ax.text(1.5, y_pos, '输出:', fontsize=12, fontweight='bold', va='center')
ax.text(3.5, y_pos, '预测值 + 损失值', fontsize=13, ha='center', va='center', color='#004D40')

# ========== 右侧：反向传播 ==========
ax.text(10.5, 8.2, '反向传播', fontsize=20, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFCDD2', edgecolor='#C62828', linewidth=2))
ax.text(10.5, 7.8, 'Backward Propagation', fontsize=11, ha='center', style='italic', color='#C62828')

# 第1行：方向
y_pos = 7.0
ax.add_patch(FancyBboxPatch((8.2, y_pos-0.3), 4.6, 0.6,
                            boxstyle='round,pad=0.1', facecolor='#E0F7FA', edgecolor='#00ACC1', linewidth=2))
ax.text(8.5, y_pos, '方向:', fontsize=12, fontweight='bold', va='center')
ax.text(10.5, y_pos, '输出 → 输入', fontsize=13, ha='center', va='center', color='#00695C')
# 箭头
ax.annotate('', xy=(9.3, y_pos), xytext=(12.3, y_pos),
            arrowprops=dict(arrowstyle='->', lw=3, color='#D32F2F'))

# 第2行：目的
y_pos = 6.0
ax.add_patch(FancyBboxPatch((8.2, y_pos-0.3), 4.6, 0.6,
                            boxstyle='round,pad=0.1', facecolor='#FFF9C4', edgecolor='#F57C00', linewidth=2))
ax.text(8.5, y_pos, '目的:', fontsize=12, fontweight='bold', va='center')
ax.text(10.5, y_pos, '计算梯度', fontsize=13, ha='center', va='center', color='#E65100')

# 第3行：计算内容
y_pos = 5.0
ax.add_patch(FancyBboxPatch((8.2, y_pos-0.3), 4.6, 0.6,
                            boxstyle='round,pad=0.1', facecolor='#E1BEE7', edgecolor='#8E24AA', linewidth=2))
ax.text(8.5, y_pos, '计算:', fontsize=12, fontweight='bold', va='center')
ax.text(10.5, y_pos, 'dloss/dw, dloss/db', fontsize=13, ha='center', va='center',
        color='#4A148C', family='monospace', fontweight='bold')

# 第4行：特点
y_pos = 4.0
ax.add_patch(FancyBboxPatch((8.2, y_pos-0.3), 4.6, 0.6,
                            boxstyle='round,pad=0.1', facecolor='#C8E6C9', edgecolor='#388E3C', linewidth=2))
ax.text(8.5, y_pos, '特点:', fontsize=12, fontweight='bold', va='center')
ax.text(10.5, y_pos, '链式法则求导', fontsize=13, ha='center', va='center', color='#1B5E20')

# 第5行：代码
y_pos = 2.8
ax.add_patch(FancyBboxPatch((8.2, y_pos-0.5), 4.6, 1.0,
                            boxstyle='round,pad=0.1', facecolor='#FFCCBC', edgecolor='#D84315', linewidth=2))
ax.text(8.5, y_pos+0.3, '代码:', fontsize=12, fontweight='bold', va='center')
ax.text(10.5, y_pos+0.15, 'optimizer.zero_grad()', fontsize=11, ha='center', va='center',
        family='monospace', color='#BF360C')
ax.text(10.5, y_pos-0.15, 'loss.backward()', fontsize=11, ha='center', va='center',
        family='monospace', color='#BF360C')
ax.text(10.5, y_pos-0.35, 'optimizer.step()', fontsize=11, ha='center', va='center',
        family='monospace', color='#BF360C')

# 第6行：结果
y_pos = 1.5
ax.add_patch(FancyBboxPatch((8.2, y_pos-0.3), 4.6, 0.6,
                            boxstyle='round,pad=0.1', facecolor='#B2DFDB', edgecolor='#00897B', linewidth=2))
ax.text(8.5, y_pos, '输出:', fontsize=12, fontweight='bold', va='center')
ax.text(10.5, y_pos, '梯度 + 更新参数', fontsize=13, ha='center', va='center', color='#004D40')

# 底部总结
ax.text(7, 0.5, '记忆要点：前向算预测，反向算梯度；梯度指方向，学习率定步幅',
        fontsize=13, ha='center', style='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFFACD', edgecolor='#FFD700', linewidth=2))

plt.tight_layout()
plt.savefig('前向传播vs反向传播对比图.png', dpi=300, bbox_inches='tight', facecolor='#FFF8E7')
print('图片已保存：前向传播vs反向传播对比图.png')
