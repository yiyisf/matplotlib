# _*_coding:utf-8
# author='sandra'
"""
练习使用散点图模式，plt.scatter, marker设置点的形状，s设置点的size
"""
from pylab import mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['SimHei'] #设置字体
mpl.rcParams['axes.unicode_minus'] = False
x = [1,2,3,4,5,6,7,8]
y = [2,4,6,3,6,7,4,6]

plt.scatter(x, y, s=50, marker='*', label='scatter', color='m')
plt.title("散点图", color='m')
plt.show()
