# -*- coding: utf-8 -*-
# author='sandra'
"""
练习修改标签及显示格式
"""
from __future__ import unicode_literals
from pylab import mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib
import time
import datetime as dt
# import csv
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei'] #设置字体
mpl.rcParams['axes.unicode_minus'] = False

x = []
y = []

#使用csv读取txt数据并解析
# with open("data/src.txt",mode='r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))

#使用numpy直接解析
# x, y = numpy.loadtxt("data/src.txt", delimiter=',', unpack=True)

#转换字符型的日期为日期型，因查询当天跟当月时返回的时间格式不同，当天时格式为unit time，当月时为YYYYMMDD
#因此增加timer以区分处理格式，YYYYMMDD时无需使用time转换.
def bytesdata2num(datefmt, timer, encoding='utf-8'):
    strconvertrt = mdates.strpdate2num(datefmt)
    def bytesconverter_day(b):
        s = time.strftime("%y%m%d %H%M", time.localtime(int(b.decode(encoding))))
        return strconvertrt(s)
    def bytesconverter(b):
        s = b.decode(encoding)
        # print(s)
        return strconvertrt(s)
    if timer == 'd':
        return bytesconverter_day
    else:
        return bytesconverter


def get_data_from_internet(stack, date):
    baseurl = "http://chartapi.finance.yahoo.com/instrument/1.0/"+ stack +"/chartdata;type=quote;range="+date+"/csv"
    sourece_code = urllib.request.urlopen(baseurl).read().decode()
    # print(sourece_code)
    stock_data = []
    split_source = sourece_code.split("\n")

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
    if 'd' in date:
        date, close, high, low, openp, volume = np.loadtxt(stock_data,
                                                           delimiter=',',
                                                           unpack=True)
                                                           # converters={0: bytesdata2num('%y%m%d %H%M', 'd')})
        dateconver = np.vectorize(dt.datetime.fromtimestamp)  #也可用此来转换日期
        date = dateconver(date)
    else:
        date, close, high, low, openp, volume = np.loadtxt(stock_data,
                                                           delimiter=',',
                                                           unpack=True,
                                                           converters={0: bytesdata2num('%Y%m%d', 'y')})

    ax1.plot_date(date, close, '-', label='从网络加载股价')
    ax1.plot([], [], label='大于平均价', color='g', alpha=0.5, linewidth=4)#设定图例根据颜色
    ax1.plot([], [], label='小于平均价', color='r', alpha=0.5, linewidth=4)
    ax1.axhline(60, color='k', linewidth=5)   #设定一条X方向的亮线
    ax1.fill_between(date, close, 60, where=(close > 60), facecolor='g', alpha=0.5)  #按价格大于60部分显示颜色
    ax1.fill_between(date, close, 60, where=(close <= 60), facecolor='r', alpha=0.5)

    ax1.spines['left'].set_color('#F2E41D') #设定左侧线的颜色
    ax1.spines['top'].set_linewidth(4)   #设定上方线的宽度

    ax1.tick_params(axis='x', colors='#1D99F2')  #设定X轴内容的颜色


    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True, linestyle='-')
    ax1.xaxis.label.set_color('m')  #设置X轴标签文字的颜色
    ax1.xaxis.label.set_color('b')  #同理设置Y轴
    plt.xlabel("时间")
    plt.ylabel("股价")
    plt.title(stack)
    plt.subplots_adjust(left=0.08, right=0.97, top=0.95, bottom=0.15)
    rect = ax1.patch
    rect.set_facecolor('c')
    plt.legend()   #plot有label选项时，必须要有此句
    plt.show()


get_data_from_internet("300468.sz", '1y')


