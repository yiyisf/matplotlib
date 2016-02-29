# _*_coding:utf-8
# author='sandra'
"""
练习使用饼状图模式，plt.pie,
"""
from pylab import mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['SimHei'] #设置字体
mpl.rcParams['axes.unicode_minus'] = False

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

days   =  [1,2,3,4,5,6,7]

eating =  [2,3,4,3,2,4,3]
play   =  [8,5,7,8,13,9,12]
working = [7,8,7,2,2,3,2]
sleep  =  [7,8,6,11,7,8,7]

slice = [2,8,7,7]
activities = ['吃饭','玩耍','工作','睡觉']
clos = ['m','c','b','r']
#以下四行添加图例
# plt.plot([],[],color='m', label='吃饭', linewidth=4)
# plt.plot([],[],color='c', label='玩耍', linewidth=4)
# plt.plot([],[],color='r', label='工作', linewidth=4)
# plt.plot([],[],color='k', label='睡觉', linewidth=4)

#以下colors不能使用color，会产生于图例中的颜色不一致
ax1.pie(slice, explode=(0,0,1,0), labels=activities, colors=clos, shadow=True, autopct='%1.1f%%')
# plt.stackplot(days, eating,play,working,sleep, colors=['m','c','r','k'])
# plt.scatter(x, y, s=50, marker='*', label='scatter', color='m')
plt.title("饼状图\n一天时间统计", color='m')
plt.legend()
# plt.show()
fig.savefig("save_image/pie.png")
plt.close(fig)