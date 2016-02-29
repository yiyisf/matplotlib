# -*- coding: utf-8 -*-
# author='sandra'
"""
练习从网络加载数据显示图形
"""
from __future__ import unicode_literals
from pylab import mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib
import time
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
        print(s)
        return strconvertrt(s)
    def bytesconverter(b):
        # s = time.strftime("%Y%m%d", time.localtime(int(b.decode(encoding))))
        s = b.decode(encoding)
        print(s)
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

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    print(stock_data)

    if 'd' in date:
        date, close, high, low, openp, volume = np.loadtxt(stock_data,
                                                           delimiter=',',
                                                           unpack=True,
                                                           converters={0: bytesdata2num('%y%m%d %H%M', 'd')})
    else:
        date, close, high, low, openp, volume = np.loadtxt(stock_data,
                                                           delimiter=',',
                                                           unpack=True,
                                                           converters={0: bytesdata2num('%Y%m%d', 'y')})
    plt.plot_date(date, close, '-', label='从网络加载股价')
    plt.xlabel("时间")
    plt.ylabel("股价")
    plt.title("练习从网络加载数据!")
    rect = plt.figure(1).patch
    rect.set_facecolor('c')
    plt.legend()   #plot有label选项时，必须要有此句
    plt.show()

get_data_from_internet("300468.sz", '1y')


