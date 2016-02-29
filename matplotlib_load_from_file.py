# -*- coding: utf-8 -*-
# author='sandra'
"""
练习从文件加载数据显示图形
"""
from __future__ import unicode_literals

import time
from pylab import mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
import numpy

mpl.rcParams['font.sans-serif'] = ['SimHei'] #设置字体以支持中文
mpl.rcParams['axes.unicode_minus'] = False

x = []
y = []
fig = plt.figure()

ax1 = fig.add_subplot(1,1,1)
#使用csv读取txt数据并解析
# with open("data/src.txt",mode='r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))


def refresh(i):
    x, y = numpy.loadtxt("data/src.txt", delimiter=',', unpack=True)
    # ax1.clear()
    ax1.plot(x, y, label='从文件加载')
    plt.xlabel("X轴")
    plt.ylabel("Y轴")
    plt.title("练习从文件加载数据!")
    # rect = ax1.patch
    # rect.set_facecolor('b')
    plt.legend()  # plot有label选项时，必须要有此句


#使用numpy直接解析
# refresh(
ant = animation.FuncAnimation(fig, refresh, interval=5000)
plt.show()
time.sleep(5)
fig.savefig("save_image/from_file.png", )
plt.close(fig)


