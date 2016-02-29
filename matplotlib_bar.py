# _*_coding:utf-8
# author='sandra'
"""
练习使用Bar，其中hist可以按bins段，统计x中的数据数量
"""
import matplotlib.pyplot as plt

x = [20,35,46,76,5,6,45,76,85,34,5,46,67,56,34,65,87,46,20,23,34,65,100,120,18,9,78]
bins = [10,20,30,40,50,60,70,80,90,100]
plt.hist(x, bins, rwidth=0.5)
plt.show()
# x = [1,3,5,7,9]
# y = [3,6,7,4,0]
# x2 = [2,4,6,8,10]
# y2 = [4,6,8,3,6]
# plt.bar(x, y, label='Bar1', color='r')
# plt.bar(x2, y2, label='Bar2', color='c')
# plt.legend()
plt.show()
