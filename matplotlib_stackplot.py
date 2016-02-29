# _*_coding:utf-8
# author='sandra'
"""
练习使用叠加图模式，plt.stackplot,
"""
from pylab import mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['SimHei'] #设置字体
mpl.rcParams['axes.unicode_minus'] = False
days   =  [1,2,3,4,5,6,7]

eating =  [2,3,4,3,2,4,3]
play   =  [8,5,7,8,13,9,12]
working = [7,8,7,2,2,3,2]
sleep  =  [7,8,6,11,7,8,7]

#以下四行添加图例
plt.plot([],[],color='m', label='吃饭', linewidth=4)
plt.plot([],[],color='c', label='玩耍', linewidth=4)
plt.plot([],[],color='r', label='工作', linewidth=4)
plt.plot([],[],color='k', label='睡觉', linewidth=4)

#以下colors不能使用color，会产生于图例中的颜色不一致
plt.stackplot(days, eating,play,working,sleep, colors=['m','c','r','k'])
# plt.scatter(x, y, s=50, marker='*', label='scatter', color='m')
plt.title("叠加图\n一周时间统计", color='m')
plt.legend()
plt.show()
