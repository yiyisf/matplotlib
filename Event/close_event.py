# _*_coding:utf-8
# author=''
from __future__ import print_function
import matplotlib.pyplot as plt


def handle_close(evt):
    print(evt)
    print('Closed Figuer!')

fig = plt.figure()
fig.canvas.mpl_connect('close_event', handle_close)

plt.text(0.35, 0.5, 'Close me!', dict(size=30))
plt.show()