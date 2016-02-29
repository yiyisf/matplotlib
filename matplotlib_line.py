# -*- coding: utf-8 -*-
# author='sandra'
"""
练习单条线或多条线图
"""
from __future__ import unicode_literals
from pylab import mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif'] = ['SimHei'] #设置字体
mpl.rcParams['axes.unicode_minus'] = False

x = [1,4,5]
y = [4,7,9]
x2 = [1,4,5]
y2 = [5,9,7]

plt.plot(x, y, label='首次')
plt.plot(x2, y2, label='二次')  #第二条线
# plt.step(x, y, label='首次')
# plt.step(x2, y2, label='二次')  #第二条线
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.title("首次练习线图")
plt.legend()   #必须要有
plt.show()


